from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
import requests
import csv
from io import TextIOWrapper
from datetime import datetime
from Gado.models import Animal, Origem

def dashboard(request):
    animais = Animal.objects.all()

    content_type = ContentType.objects.get_for_model(Animal)
    latest_actions = LogEntry.objects.filter(content_type=content_type).order_by('-action_time')[:10]
    total_animais = animais.count()
    total_nelore = animais.filter(raca__nome='NELORE').count()
    total_macho = animais.filter(sexo='M').count()
    total_femea = animais.filter(sexo='F').count()

    # Função para obter o valor do arroba
    def get_arroba_value():
        try:
            api_url = 'https://www.scotconsultoria.com.br/json/corteva/?cotacao=boigordo'
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                cotacoes = data.get('Cotacao', [])
                valores = cotacoes[6].get('Reais_Avista', None)
                return f'R$ {valores}' if valores else 'Valor não disponível'
            else:
                return 'Valor não disponível'
        except Exception as e:
            return 'Erro ao consultar a API'

    # Chamada da função para obter o valor do arroba
    valor_do_arroba = get_arroba_value()

    context = {
        'animais': animais,
        'latest_actions': latest_actions,
        'total_animais': total_animais,
        'valor_do_arroba': valor_do_arroba,
        'total_nelore': total_nelore,
        'total_macho': total_macho,
        'total_femea': total_femea,
    }

    return render(request, 'pages/index.html', context)

def home(request):
    return redirect('dashboard')

def edit_animal(request):
    return redirect('dashboard')


# TESTE DE IMPORTACAO EM MASSA
def convert_data(data_str):
    # Função auxiliar para converter a data no formato correto
    if data_str:
        try:
            return datetime.strptime(data_str, '%d.%m.%Y').strftime('%Y-%m-%d')
        except ValueError:
            return None
    return None
def importar_animais(request):
    if request.method == 'POST':
        # Verificar se um arquivo foi enviado na requisição
        if 'file' in request.FILES:
            arquivo = request.FILES['file']
            if arquivo.name.endswith('.csv'):
                # Ler o arquivo CSV e tratar erros de codificação
                try:
                    csv_file = TextIOWrapper(arquivo, encoding='utf-8-sig')
                except UnicodeDecodeError:
                    return render(request, 'pages/importacao_erro.html', {'erro_msg': 'Erro de codificação do arquivo.'})

                reader = csv.DictReader(csv_file)

                for row in reader:
                    print(row)
                    try:
                        # Converter o formato da data para "YYYY-MM-DD"
                        data_nascimento = None
                        if row['data_nascimento']:
                            data_nascimento = convert_data(row['data_nascimento'])

                        # Demais campos do seu modelo

                        # Buscar ou criar a instância do modelo 'Origem'
                        origem, _ = Origem.objects.get_or_create(nome=row['origem'])

                        # Criar o objeto 'Animal' no banco de dados com os dados da linha atual
                        Animal.objects.create(
                            brinco=row['brinco'],
                            sexo=row['sexo'],
                            origem=origem,  # Atribuir a instância do modelo 'Origem'
                            data_compra=row['data_compra'],
                            data_nascimento=row['data_nascimento'] if row['data_nascimento'] else None,
                            raca_id=row['raca'] if row['raca'] else None,  # Usar o campo raca_id para atribuir a chave estrangeira
                            tipo_id=row['tipo'] if row['tipo'] else None,  # Usar o campo tipo_id para atribuir a chave estrangeira
                            idade=row['idade'] if row['idade'] else None,
                            status_id=row['status'] if row['status'] else None,  # Usar o campo status_id para atribuir a chave estrangeira
                            pasto_id=row['pasto'] if row['pasto'] else None,  # Usar o campo pasto_id para atribuir a chave estrangeira
                            caracteristica_id=row['caracteristica'] if row['caracteristica'] else None,  # Usar o campo caracteristica_id para atribuir a chave estrangeira
                            observacoes=row['observacoes'],
                            nome_pai=row['nome_pai'],
                            nome_mae=row['nome_mae'],
                            data_entrada=row['data_entrada'] if row['data_entrada'] else None,
                            data_desmama=row['data_desmama'] if row['data_desmama'] else None,
                            peso=row['peso'] if row['peso'] else None,
                            campo_id=row['campo'] if row['campo'] else None,  # Usar o campo campo_id para atribuir a chave estrangeira
                            data_morte=row['data_morte'] if row['data_morte'] else None,
                            motivo_morte_id=row['motivo_morte'] if row['motivo_morte'] else None,  # Usar o campo motivo_morte_id para atribuir a chave estrangeira
                        )

                    except KeyError as e:
                        # Caso algum campo obrigatório não esteja presente no CSV
                        print({e})
                        return render(request, 'pages/importacao_erro.html', {'erro_msg': f'Campo obrigatório ausente: {e}'})

                    except Exception as e:
                        # Lidar com outros erros durante o processamento
                        print({e})
                        return render(request, 'pages/importacao_erro.html', {'erro_msg': f'Erro durante o processamento: {e}'})

                return render(request, 'pages/importacao_sucesso.html')
            else:
                return render(request, 'pages/importacao_erro.html', {'erro_msg': 'O arquivo deve estar no formato CSV.'})
        else:
            return render(request, 'pages/importacao_erro.html', {'erro_msg': 'Nenhum arquivo foi enviado na requisição.'})

    return render(request, 'pages/importar_animais.html')
