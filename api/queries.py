READ_COMPANIES_AND_VACANCIES_COUNT: str = (
    """
    SELECT c.company_name, COUNT(v.hh_id)
    FROM companies as c
    JOIN vacancies as v ON c.company_id = v.company_id
    GROUP BY c.company_name;
    """
)

READ_ALL_VACANCIES: str = (
    """
     SELECT c.company_name, v.vacancy_name, v.salary, v.vacancy_url
     FROM companies as c
     JOIN vacancies as v ON c.company_id = v.company_id;
    """
)

READ_VACANCIES_AVG_SALARY: str = (
    """
    SELECT AVG(salary)
    FROM vacancies
    WHERE salary <> 0;
    """
)


READ_VACANCIES_WITH_HIGHER_SALARY: str = (
    """
    SELECT vacancy_name, salary, vacancy_url
    FROM vacancies
    WHERE salary > (SELECT AVG(salary) 
                    FROM vacancies 
                    WHERE salary <> 0);
    """
)

READ_VACANCIES_BY_KEYWORD: str = (
    """
    SELECT vacancy_name, salary, vacancy_url
    FROM vacancies
    WHERE vacancy_name LIKE '%{keyword}%';
    """
)
