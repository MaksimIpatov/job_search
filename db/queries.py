CREATE_DATABASE: str = """CREATE DATABASE {dbname};"""

CREATE_TABLE_COMPANIES: str = (
    """
    CREATE TABLE IF NOT EXISTS companies (
            company_id int NOT NULL,
            company_name VARCHAR(128) NOT NULL
        );
    """
)

CREATE_TABLE_VACANCIES: str = (
    """
    CREATE TABLE IF NOT EXISTS vacancies (
            vacancy_id SERIAL,
            hh_id BIGINT,
            vacancy_name VARCHAR(128) NOT NULL,
            vacancy_url VARCHAR(255) NOT NULL,
            salary BIGINT,
            schedule VARCHAR(255),
            company_id int NOT NULL,
            CONSTRAINT pk_vacancies_vacancy_id PRIMARY KEY (vacancy_id)
        );
    """
)

INSERT_INTO_COMPANIES: str = (
    """
    INSERT INTO companies (company_id, company_name)
    VALUES (%s, %s);
    """
)

INSERT_INTO_VACANCIES: str = (
    """
     INSERT INTO vacancies (hh_id, 
                            vacancy_name, 
                            vacancy_url, 
                            salary, 
                            schedule, 
                            company_id)
     VALUES (%s, %s, %s, %s, %s, %s);
    """
)
