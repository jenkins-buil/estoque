from sqlalchemy import create_engine

from sqlalchemy.orm import Session



schema_name = "estoque"

engine_schema = create_engine('mysql+pymysql://root:mudar123@mysql-container:3306')

engine_schema.execute(f"CREATE SCHEMA IF NOT EXISTS {schema_name};")

engine = create_engine('mysql+pymysql://root:mudar123@mysql-container:3306/estoque')


session = Session()