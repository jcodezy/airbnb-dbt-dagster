from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets


from .constants import dbt_manifest_path


@dbt_assets(manifest=dbt_manifest_path)
def dbtlearn_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()


# daily_partitions = DailyPartitionsDefinition(start_date='2024-01-01')
