# Kenzie Pet

Uma API desenvolvida para guardar e disponibilizar informações de animais em PetShops.


## Instalação
#### No terminal, siga os seguintes passos:
Crie uma pasta na sua máquina e baixe o projeto:

    git clone https://gitlab.com/Haguken/kenzie-pet.git
<br>
Entre na pasta, crie um ambiente virtual e entre nele:

    cd kenzie-pet && python3 -m venv venv && source venv/bin/activate
<br>
Instale as dependências:

    pip install -r requirements.txt
<br>
Crie as tabelas do banco de dados:

    python3 manage.py migrate
<br>
Rode o sistema em http://127.0.0.1:8000/ digitando:

    python3 manage.py runserver
<br>

## Utilização
É requerido um API client como, por exemplo, o [Postman](https://www.postman.com/downloads/)
### Rotas:
<br>

#### GET /api/animals/

    RESPONSE STATUS -> HTTP 200 (ok)

Response:

    [
      {
        "id": 1,
        "name": "Bidu",
        "age": 1.0,
        "weight": 30.0,
        "sex": "macho",
        "group": {
          "id": 1,
          "name": "cao",
          "scientific_name": "canis familiaris"
        },
        "characteristic_set": [
          {
            "id": 1,
            "characteristic": "peludo"
          },
          {
            "id": 2,
            "characteristic": "medio porte"
          }
        ]
      },
      {
        "id": 2,
        "name": "Hanna",
        "age": 1.0,
        "weight": 20.0,
        "sex": "femea",
        "group": {
          "id": 2,
          "name": "gato",
          "scientific_name": "felis catus"
        },
        "characteristic_set": [
          {
            "id": 1,
            "characteristic": "peludo"
          },
          {
            "id": 3,
            "characteristic": "felino"
          }
        ]
      }
    ]
    <br>
    
#### GET /api/animals/<int:animal_id>/
Esta rota retorna as informações do animal com id igual ao passado na rota.

    RESPONSE STATUS -> HTTP 200 (ok)

Response:

    {
      "id": 1,
      "name": "Bidu",
      "age": 1.0,
      "weight": 30.0,
      "sex": "macho",
      "group": {
        "id": 1,
        "name": "cao",
        "scientific_name": "canis familiaris"
      },
      "characteristic_set": [
        {
          "id": 1,
          "characteristic": "peludo"
        },
        {
          "id": 2,
          "characteristic": "medio porte"
        }
      ]
    }
<br>

#### POST /api/animals/
Esta rota é para a criação de informações de animais.

    RESPONSE STATUS -> HTTP 201 (created)
  Body:
  

    {
      "name": "Bidu",
      "age": 1,
      "weight": 30,
      "sex": "macho",
      "group": {
        "name": "cao",
        "scientific_name": "canis familiaris"
      },
      "characteristic_set": [
        {
          "characteristic": "peludo"
        },
        {
          "characteristic": "medio porte"
        }
      ]
    }
Response:

    {
      "id": 1,
      "name": "Bidu",
      "age": 1.0,
      "weight": 30.0,
      "sex": "macho",
      "group": {
        "id": 1,
        "name": "cao",
        "scientific_name": "canis familiaris"
      },
      "characteristic_set": [
        {
          "id": 1,
          "characteristic": "peludo"
        },
        {
          "id": 2,
          "characteristic": "medio porte"
        }
      ]
    }

 #### DELETE /api/animals/<int:animal_id>/
Rota para deletar as informações de um animal.

Não há conteúdo no retorno da requisição.

    RESPONSE STATUS -> HTTP 204 (no content)
## Tecnologias usadas
- Django
- Djando Rest Framework
- SQLite
## License
MIT
