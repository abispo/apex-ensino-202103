"""
Conta Corrente Via Credi
Conta Celesc

Transaction
Conta Debitada -> CC Via Credi
Conta Creditada -> Conta Celesc

"""

from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.run()
