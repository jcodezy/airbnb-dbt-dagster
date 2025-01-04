# DBT/Dagster Project: Airbnb Data  

### Description 
This repo contains my hands-on exercises, experiments, and best practices for using dbt to manage data transformations from the Udemy course 'The Complete dbt (Data Build Tool) Bootcamp: Zero to Hero'. 

We string together: Snowflake, DBT and then Dagster to build a data pipeline ready to serve analytics users with data and charts in Preset. 

### The Project 
The DBT project goes over the essential building blocks of DBT: creating models, setting up macros, building tests, and putting it all together with Dagster to orchestrate our dbt tasks in a production-like scenario. 

### Goals of the Project 
1. Understanding dbt model structure and relationships.
    - Implement staging and mart layers for transformations. 
2. Practicing SQL transformations with Jinja templating.
    - Learn how different dbt models reference each other using {{ ref }} 
- Learning how to set up CI/CD or testing in dbt, etc.

### Project Structure 
dbt
    - dbt_dagster_project 
        - dbt_dagster_project 
            - assets.py 
            - constants.py 
            - definitions.py
            - schedules.py 
    - dbtlearn 
        - analyses
        - assets 
            - Images and other assets used for dbt docs. 
        - dbt_packages 
        - logs
        - macros
        - models 
            - Database tables to be materialized. 
        - seeds
            - Data sources from CSVs. 
        - snapshots
        - target
        - tests 
            - Generic and singular tests.
        - dbt_project.yml
        - packages.yml 
    - requirements.txt 


### How to Run 
1. Clone repository 
2. Install dependencies 
    - Run ```pip install -r requirements.txt``` 
3. Sign up for free Snowflake account 
    - Get your account, database, password, role and schema details for next step. 
4. Configure dbt 
    - Your dbt profile should be located in ~/.dbt/profiles.yml 
    - To view your dbt profile, run ```cat ~/.dbt/profiles.yml``` or ```less ~/.dbt/profiles.yml``` 
    - Your ~/.dbt/profiles.yml profile should look like: 
        - dev:
            - account: <YOUR_ACCOUNT>
            - database: AIRBNB
            - password: <YOUR_PASSWORD>
            - role: <YOUR_ROLE>
            - schema: DEV
            - threads: 1
            - type: snowflake
5. Run dbt 
    - ```dbt compile```
    - ```dbt run``` 
    - ```dbt test``` 

6. Create a Dagster project from an existing dbt project 
    - Fill in your dbt project directory and run ```dagster-dbt project scaffold --project-name dbt_dagster_project --dbt-project-dir=<YOUR_PROJ_DIR>```

7. Start Dagster
```cd dbt_dagster_project && $env:DAGSTER_DBT_PARSE_PROJECT_ON_LOAD = 1 && dagster dev```