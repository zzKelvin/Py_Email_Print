#Cria o banco de dados
import peewee

db = peewee.SqliteDatabase('Data.db')


class BaseModel(peewee.Model):

    class Meta:
        database = db

class Emails(BaseModel):

    N_Email = peewee.IntegerField()
    Possui_Banco = peewee.IntegerField()

if __name__ == '__main__':
    try:
        Emails.create_table()
        print("Tabela 'Data' criada com sucesso!")
    except peewee.OperationalError:
        print("Tabela 'Data' ja existe!")
