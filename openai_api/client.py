from openai import OpenAI

client = OpenAI(api_key='API_KEY')

def get_car_ai_bio(model, brand, year):
    message ='''Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.'''
    message = message.format(brand, model, year)
    response = client.chat.completions.create(
        messages = [
            {
                'role':'user',
                'content': message
            }
        ],
        model = 'gpt-3.5-turbo',
        max_tokens = 1000, # resposta nao exceda 1000 tokens
    )
    return response['choices'][0]['text']