import copy
import datetime
import decimal
import json
import os
import pytest

from sqlalchemy import create_engine, Column, Index, Table, select
from sqlalchemy.dialects import postgresql
from sqlalchemy.engine.url import URL
from sqlalchemy.sql import func, text, sqltypes
from sqlalchemy.schema import AddConstraint, DropConstraint, ForeignKeyConstraint, MetaData

from pg_database import conf
from pg_database.conf import PgDatabaseSettings
from pg_database.schema import create_foreign_key, create_column, create_index, create_table, create_tsvector_column
from pg_database.schema import alter_column_type, drop_foreign_key, drop_column, drop_index, drop_table
from pg_database.sql import query_tsvector_columns, query_json_keys
from pg_database.schema import get_table, get_table_count, get_tables, has_index, table_exists
from pg_database.sql import insert_from, insert_into, select_from, select_into, update_from, update_rows
from pg_database.types import DATE_FORMAT, DATETIME_FORMAT


DJANGO_SETTINGS_VAR = conf.DJANGO_SETTINGS_VAR
ENVIRONMENT_VARIABLE = conf.ENVIRONMENT_VARIABLE
DEFAULT_ENGINE = conf.DEFAULT_ENGINE
DEFAULT_PORT = conf.DEFAULT_PORT
DEFAULT_USER = conf.DEFAULT_USER

DEFAULT_DJANGO_DB = conf.DEFAULT_DJANGO_DB
DEFAULT_DATE_FORMAT = conf.DEFAULT_DATE_FORMAT
DEFAULT_TIMESTAMP_FORMAT = conf.DEFAULT_TIMESTAMP_FORMAT

DATABASE_INFO = conf.settings.database_info
DATABASE_NAME = conf.settings.database_name
SITE_TABLE_NAME = "site_table"
ALL_TEST_TABLES = (SITE_TABLE_NAME, f"test_{SITE_TABLE_NAME}", f"tmp_{SITE_TABLE_NAME}")

SITE_COL_TYPES = {
    "pk": sqltypes.Integer,
    "obj_order": sqltypes.Numeric,
    "obj_hash": sqltypes.Text,
    "site_json": postgresql.json.JSONB,
    "test_bool": sqltypes.Boolean,
    "test_date": sqltypes.Date,
    "test_json": postgresql.json.JSONB,
    "test_none": sqltypes.Text,
}
SITE_TABLE_COLS = (
    "pk",
    "obj_hash",
    "obj_order",
    "site_addr",
    "site_city",
    "site_state",
    "site_zip",
    "site_json",
    "countyname",
    "test_bool",
    "test_date",
    "test_geom",
    "test_json",
    "test_none"
)
SEARCHABLE_COLS = ("obj_hash", "site_addr", "site_city", "site_state", "site_zip", "countyname")

SITE_TEST_DATA = [
    {
        "pk": "0",
        "obj_hash": "0-0-7350-12224",
        "obj_order": 0,
        "site_addr": "7350 STATE ST",
        "site_city": "ALBANY",
        "site_state": "NY",
        "site_zip": "12224",
        "site_json": {"number": "7350", "street": "STATE ST", "city": "ALBANY", "state": "NY"},
        "countyname": "Albany",
        "test_bool": 1,
        "test_date": datetime.datetime.strptime("2020-02-02 00:00:00", DATETIME_FORMAT),
        "test_json": {"data": [1, 2, 3]},
        "test_geom": None,
        "test_none": "null",
    },
    {
        "pk": "1",
        "obj_hash": "1-9-7350-12224",
        "obj_order": 9,
        "site_addr": "7350 STATE ST",
        "site_city": "ALBANY",
        "site_state": "NY",
        "site_zip": "12224",
        "site_json": {"number": "7350", "street": "STATE ST", "city": "ALBANY", "state": "NY"},
        "countyname": "Albany",
        "test_bool": 0,
        "test_date": datetime.datetime.strptime("2010-01-01", DATE_FORMAT),
        "test_json": ["one", "two", "three"],
        "test_geom": None,
        "test_none": None,
    },
    {
        "pk": "2",
        "obj_hash": "2-1-7350-12224",
        "obj_order": 1,
        "site_addr": "7350 STATE ST APT 1100",
        "site_city": "ALBANY",
        "site_state": "NY",
        "site_zip": "12224",
        "site_json": {"number": "7350", "street": "STATE ST", "unit": "1100", "city": "ALBANY", "state": "NY"},
        "countyname": "Albany",
        "test_bool": 0.0,
        "test_date": datetime.datetime.strptime("2020-01-02 00:00:00", DATETIME_FORMAT).date(),
        "test_json": [],
        "test_geom": None,
        "test_none": "",
    },
    {
        "pk": "3",
        "obj_hash": "3-8-7450-12224",
        "obj_order": 8,
        "site_addr": "7450 STATE ST",
        "site_city": "ALBANY",
        "site_state": "NY",
        "site_zip": "12224",
        "site_json": {"number": "7450", "street": "STATE ST", "city": "ALBANY", "state": "NY"},
        "countyname": "Albany",
        "test_bool": 1.0,
        "test_date": datetime.datetime.strptime("2010-02-02", DATE_FORMAT).date(),
        "test_json": {},
        "test_geom": None,
        "test_none": "[]",
    },
    {
        "pk": "4",
        "obj_hash": "4-2-7450-12224",
        "obj_order": 2,
        "site_addr": "7450 STATE ST APT 1101",
        "site_city": "ALBANY",
        "site_state": "NY",
        "site_zip": "12224",
        "site_json": {"number": "7450", "street": "STATE ST", "unit": "1101", "city": "ALBANY", "state": "NY"},
        "countyname": "Albany",
        "test_bool": False,
        "test_date": "2020-02-01",
        "test_json": {"id": 4, "hash": "4-2-7450-12224"},
        "test_geom": None,
        "test_none": "{}",
    },
    {
        "pk": "5",
        "obj_hash": "5-7-7550-12224",
        "obj_order": 7,
        "site_addr": "7550 STATE AVE",
        "site_city": "ALBANY",
        "site_state": "NY",
        "site_zip": "12224",
        "site_json": {"number": "7550", "street": "STATE ST", "city": "ALBANY", "state": "NY"},
        "countyname": "Albany",
        "test_bool": None,
        "test_date": "2010-02-01",
        "test_json": {"county": "Albany", "city": "ALBANY"},
        "test_geom": None,
        "test_none": "0",
    },
    {
        "pk": "6",
        "obj_hash": "6-3-7550-12224",
        "obj_order": 3,
        "site_addr": "7550 STATE ST NORTH",
        "site_city": "ALBANY",
        "site_state": "NY",
        "site_zip": "12224",
        "site_json": {"number": "7550", "street": "STATE ST NORTH", "city": "ALBANY", "state": "NY"},
        "countyname": "Albany",
        "test_bool": True,
        "test_date": "2020-04-04",
        "test_json": {"state": "NY", "zip": "https://calendar.google.com/"},
        "test_geom": None,
        "test_none": "NaN",
    },
    {
        "pk": "7",
        "obj_hash": "7-6-7550-12224",
        "obj_order": 6,
        "site_addr": "7550 STATE ST APT 1",
        "site_city": "ALBANY",
        "site_state": "NY",
        "site_zip": "12224",
        "site_json": {"number": "7550", "street": "STATE ST", "unit": "1", "city": "ALBANY", "state": "NY"},
        "countyname": "Albany",
        "test_bool": 1,
        "test_date": "2020-03-03",
        "test_json": "7-6-7550-12224",
        "test_geom": None,
        "test_none": "false",
    },
    {
        "pk": "8",
        "obj_hash": "8-4-7550-12224",
        "obj_order": 4,
        "site_addr": "7550 STATE ST STE CML5",
        "site_city": "ALBANY",
        "site_state": "NY",
        "site_zip": "12224",
        "site_json": {"number": "7550", "street": "STATE ST STE CML5", "city": "ALBANY", "state": "NY"},
        "countyname": "Albany",
        "test_bool": True,
        "test_date": "2012-12-12",
        "test_json": 8,
        "test_geom": None,
        "test_none": "undefined",
    },
]
SITE_DATA_DICT = {obj["pk"]: obj for obj in SITE_TEST_DATA}


def assert_index(meta, table_name, column_name=None, index_name=None, exists=True):

    assert index_name or column_name

    test_table = refresh_metadata(meta).tables[table_name]

    if column_name:
        assert exists == any([column_name in i.columns for i in test_table.indexes])
    if index_name:
        index_query = (
            "SELECT TRUE FROM pg_catalog.pg_indexes "
            f"WHERE tablename = '{table_name}' AND indexname = '{index_name}'"
        )
        assert exists == (meta.bind.execute(index_query).scalar() or False)


def assert_records(meta, table_name, target_data, target_columns=None, target_count=None):

    def to_date(val):
        if type(val) is datetime.date:
            return val
        elif isinstance(val, datetime.datetime):
            return val.date()
        elif isinstance(val, str):
            return datetime.datetime.strptime(val.split()[0], DATE_FORMAT).date()

    test_table = refresh_metadata(meta).tables[table_name]

    # Test the expected count of records
    target_count = len(target_data) if target_count is None else target_count
    assert select([func.count()]).select_from(test_table).scalar() == target_count

    # Test the value of each record as identified by "pk"
    for record in (dict(row) for row in test_table.select().execute()):
        pk = record["pk"]
        target = target_data[pk if pk in target_data else str(pk)]
        fields = target_columns or list(target)

        for field in (f for f in record if f in fields):
            target_val = target[field]
            record_val = record[field]

            if isinstance(record_val, bool):
                assert record_val == bool(target_val)
            elif isinstance(record_val, datetime.date):
                assert to_date(record_val) == to_date(target_val)
            elif isinstance(record_val, (int, float, decimal.Decimal)):
                assert float(record_val) == float(target_val)
            elif isinstance(record_val, (dict, list, set, tuple)):
                assert record_val == target_val
            else:
                assert str(record_val) == str(target_val)


def assert_table(meta, table_name, target_columns):

    # Test that table exists
    tables = refresh_metadata(meta).tables
    assert table_name in tables
    assert tables[table_name].exists

    # Test that all columns were inserted
    test_table = tables[table_name]
    assert len(target_columns) == len(test_table.columns)
    assert all(c in test_table.columns for c in target_columns)


def make_table(meta, table_name, columns, col_types=None, data=None, dropfirst=True):

    exists = table_name in meta.tables and meta.tables[table_name].exists

    if exists and dropfirst:
        meta.tables[table_name].drop()

    if table_name in meta.tables:
        test_table = meta.tables[table_name]
    else:
        types = col_types or SITE_COL_TYPES
        test_table = Table(table_name, meta, *[Column(col, types.get(col, sqltypes.Text)) for col in columns])
        test_table.create()

    values = list(data.values()) if isinstance(data, dict) else data

    if values:
        with test_table.metadata.bind.connect() as conn:
            conn.execute(test_table.delete())
            conn.execute(test_table.insert(), values)

    return test_table


def refresh_metadata(meta):
    metadata = MetaData(meta.bind)
    metadata.reflect()
    return metadata


@pytest.fixture()
def db_settings():

    db_env = os.environ.pop(ENVIRONMENT_VARIABLE, "")
    dj_env = os.environ.pop(DJANGO_SETTINGS_VAR, "")

    settings = conf.settings

    yield {
        ENVIRONMENT_VARIABLE: db_env,
        DJANGO_SETTINGS_VAR: dj_env,
        "DJANGO_CONFIGURED": settings._django_settings is not settings.empty
    }

    if db_env:
        os.environ[ENVIRONMENT_VARIABLE] = db_env
    if dj_env:
        os.environ["DJANGO_SETTINGS_MODULE"] = dj_env
        reload_django_settings(settings)


def reload_django_settings(db_settings):
    try:
        db_settings._django_settings._wrapped = db_settings.empty
    except Exception:
        pass


def test_conf_settings_init(db_settings):

    db_env = db_settings[ENVIRONMENT_VARIABLE]

    # Should not raise errors

    conf.settings._init_database_config()
    conf.settings._init_django_settings()
    conf.settings._init_database_info()

    # Test with invalid database configurations

    os.environ[ENVIRONMENT_VARIABLE] = db_env.replace("json", "txt")
    with pytest.raises(EnvironmentError, match="Invalid database configuration file"):
        PgDatabaseSettings()

    os.environ[ENVIRONMENT_VARIABLE] = db_env.replace("config", "nope")
    with pytest.raises(EnvironmentError, match="Database configuration file does not exist"):
        PgDatabaseSettings()

    os.environ[ENVIRONMENT_VARIABLE] = db_env.replace("test_config", "not")
    with pytest.raises(EnvironmentError, match="Database configuration file does not contain JSON"):
        PgDatabaseSettings()


def test_conf_settings_dbinfo(db_settings):

    db_env = db_settings[ENVIRONMENT_VARIABLE]
    dj_env = db_settings[DJANGO_SETTINGS_VAR]

    django_configured = db_settings["DJANGO_CONFIGURED"]
    no_config_message = "No database configuration available"
    config_key_message = "Database configuration missing required key"
    invalid_dj_message = config_key_message if django_configured else no_config_message

    # Test with no settings configured
    with pytest.raises(EnvironmentError, match=no_config_message):
        reload_django_settings(conf.settings)
        PgDatabaseSettings().database_info

    # Test with no db config and broken Django settings
    os.environ[DJANGO_SETTINGS_VAR] = dj_env.replace("settings", "not_settings")
    with pytest.raises(EnvironmentError, match=no_config_message):
        reload_django_settings(conf.settings)
        PgDatabaseSettings().database_info

    # Test with no db config and invalid Django settings
    os.environ[DJANGO_SETTINGS_VAR] = dj_env.replace("settings", "invalid_settings")
    with pytest.raises(EnvironmentError, match=invalid_dj_message):
        reload_django_settings(conf.settings)
        PgDatabaseSettings().database_info

    # Test with invalid db config and Django settings
    os.environ[ENVIRONMENT_VARIABLE] = db_env.replace("test_config", "invalid_config")
    with pytest.raises(EnvironmentError, match=config_key_message):
        reload_django_settings(conf.settings)
        PgDatabaseSettings().database_info

    # Test with valid db config and Django settings

    os.environ[ENVIRONMENT_VARIABLE] = db_env
    os.environ["DJANGO_SETTINGS_MODULE"] = dj_env
    reload_django_settings(conf.settings)


def test_conf_settings_props():

    settings = conf.settings
    django_configured = settings._django_settings is not settings.empty

    # Test non-database properties

    test_settings = PgDatabaseSettings()

    assert test_settings.django_db_key == "default"
    assert test_settings.date_format == DEFAULT_DATE_FORMAT
    assert test_settings.timestamp_format == DEFAULT_TIMESTAMP_FORMAT

    # Test database info dict

    test_settings = PgDatabaseSettings()

    conf_engine = DEFAULT_ENGINE
    conf_name = "pg_database"
    conf_port = DEFAULT_PORT
    conf_host = None
    conf_user = "django" if django_configured else DEFAULT_USER
    conf_pass = None

    assert test_settings.database_info["drivername"] == conf_engine
    assert test_settings.database_info["database"] == conf_name
    assert test_settings.database_info["port"] == conf_port
    assert test_settings.database_info["host"] == conf_host
    assert test_settings.database_info["username"] == conf_user
    assert test_settings.database_info["password"] == conf_pass

    # Test top-level database properties

    test_settings = PgDatabaseSettings()

    for prop in ("database_engine", "engine", "drivername"):
        assert getattr(test_settings, prop) == conf_engine
    for prop in ("database_name", "name", "database"):
        assert getattr(test_settings, prop) == conf_name
    for prop in ("database_port", "port"):
        assert getattr(test_settings, prop) == conf_port
    for prop in ("database_host", "host"):
        assert getattr(test_settings, prop) == conf_host
    for prop in ("database_user", "user", "username"):
        assert getattr(test_settings, prop) == conf_user
    for prop in ("database_password", "password"):
        assert getattr(test_settings, prop) == conf_pass

    # Test invalid top-level database properties (no dashes allowed)

    invalid_props = (
        "database-engine", "database-name", "database-port",
        "database-host", "database-user", "database-password"
    )
    for prop in invalid_props:
        assert getattr(test_settings, prop) is None

    # Test django database dict

    test_settings = PgDatabaseSettings()

    django_engine = "django.db.backends.postgresql" if django_configured else None
    django_name = conf_name if django_configured else None
    django_port = None
    django_host = None
    django_user = "django" if django_configured else None
    django_pass = None

    if not django_configured:
        assert test_settings.django_database == {}
    else:
        assert test_settings.django_database["django_engine"] == django_engine
        assert test_settings.django_database["django_name"] == conf_name
        assert test_settings.django_database["django_user"] == conf_user

    # Test django-specific database properties

    test_settings = PgDatabaseSettings()

    for prop in ("ENGINE", "django_engine"):
        assert getattr(test_settings, prop) == django_engine
    for prop in ("NAME", "django_name"):
        assert getattr(test_settings, prop) == django_name
    for prop in ("PORT", "django_port"):
        assert getattr(test_settings, prop) == django_port
    for prop in ("HOST", "django_host"):
        assert getattr(test_settings, prop) == django_host
    for prop in ("USER", "django_user"):
        assert getattr(test_settings, prop) == django_user
    for prop in ("PASSWORD", "django_password"):
        assert getattr(test_settings, prop) == django_pass

    # Test invalid django-specific database properties

    for prop in ("Engine", "Name", "Port", "Host", "User", "Password"):
        assert getattr(test_settings, prop) is None


def db_create(postgres_engine):

    database_exists = postgres_engine.execute(
        f"SELECT TRUE FROM pg_catalog.pg_database WHERE datname='{DATABASE_NAME}'"
    )
    if database_exists.scalar():
        return

    postgres_engine.execute(f"CREATE DATABASE {DATABASE_NAME} ENCODING 'utf8'")

    database_engine = create_engine(URL(
        drivername=DATABASE_INFO["drivername"],
        database=DATABASE_INFO["database"],
        username="postgres",
    ))
    with database_engine.connect() as conn:
        conn.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
        conn.execute("CREATE EXTENSION IF NOT EXISTS postgis_topology;")


def db_drop(postgres_engine):

    with postgres_engine.connect() as conn:
        conn.execute(
            "SELECT pg_terminate_backend(pid) FROM pg_catalog.pg_stat_activity "
            f"WHERE pid <> pg_backend_pid() AND datname = '{DATABASE_NAME}'"
        )
        conn.execute(f"DROP DATABASE {DATABASE_NAME}")


@pytest.fixture(scope='session')
def db_engine():

    postgres_engine = create_engine("postgresql:///postgres", isolation_level="AUTOCOMMIT")

    db_create(postgres_engine)
    engine = create_engine(URL(**DATABASE_INFO))

    yield engine

    engine.dispose()
    db_drop(postgres_engine)

    postgres_engine.dispose()


@pytest.fixture
def db_metadata(db_engine):
    """ Provides setup and teardown functionality for database tests """

    # Setup: create data table with indexes, and return metadata

    meta = MetaData(db_engine)
    meta.reflect()

    test_table = make_table(meta, SITE_TABLE_NAME, SITE_TABLE_COLS, data=SITE_TEST_DATA)

    # Drop and recreate test_geom as a point geometry column
    geom_sql = (
        f"ALTER TABLE {SITE_TABLE_NAME} DROP COLUMN test_geom;"
        f"ALTER TABLE {SITE_TABLE_NAME} ADD COLUMN test_geom geometry(Point,4326);"
    )
    with db_engine.connect() as conn:
        conn.execute(text(geom_sql).execution_options(autocommit=True))

    # Create unique indexes on pk and obj_order
    Index("obj_index", "pk", unique=True, _table=test_table).create()
    Index("order_index", "obj_order", unique=True, _table=test_table).create()
    Index("hash_index", "obj_hash", unique=True, _table=test_table).create()

    # Create search index on primary test data columns
    expressions = (func.to_tsvector("english", text("||' '||".join(SEARCHABLE_COLS))),)
    Index("tsvector_index", *expressions, postgresql_using="gin", _table=test_table).create()

    yield test_table.metadata

    # Teardown: drop all data related tables used in the tests

    meta = refresh_metadata(meta)
    tables = (t for t in meta.tables.values() if t.name in ALL_TEST_TABLES)
    for fk in (c for t in tables for c in t.foreign_key_constraints):
        DropConstraint(fk, cascade=True).execute(meta.bind)

    meta = refresh_metadata(meta)
    for test_table in (t for t in meta.tables.values() if t.name in ALL_TEST_TABLES):
        test_table.drop()


def test_database_setup(db_metadata):
    database_query = db_metadata.bind.execute(
        "SELECT TRUE FROM pg_catalog.pg_database "
        f"WHERE datname='{DATABASE_NAME}'"
    )
    assert database_query.scalar()


def test_create_index(db_metadata):
    table_name = SITE_TABLE_NAME
    test_table = db_metadata.tables[table_name]

    inject_sql = "DROP USER 'postgres' IF EXISTS"

    # Test with invalid parameters

    with pytest.raises(ValueError, match="No table named"):
        create_index("nope", "site_addr")
    with pytest.raises(ValueError, match="Invalid index column names"):
        create_index(table_name, [])
    with pytest.raises(ValueError, match="Invalid index column names"):
        create_index(table_name, ["site_addr", "nope"])
    with pytest.raises(ValueError, match="Invalid index column names"):
        create_index(table_name, ["site_addr", inject_sql])
    with pytest.raises(ValueError, match="Invalid index operation for multiple columns"):
        create_index(table_name, "test_json,test_none", None, "json_full")
    with pytest.raises(ValueError, match="Invalid index operation for multiple columns"):
        create_index(table_name, "test_json,test_none", None, "json_path")
    with pytest.raises(ValueError, match="Invalid index operation for multiple columns"):
        create_index(table_name, "site_addr,test_none", None, "spatial")
    with pytest.raises(ValueError, match="Invalid column type for spatial index"):
        create_index(table_name, "site_addr", None, "spatial")
    with pytest.raises(ValueError, match="Unsupported index type"):
        create_index(table_name, "site_addr", None, "nope")

    # Test default index creation
    column_name = "site_addr"
    create_index(table_name, column_name)
    assert_index(db_metadata, table_name, column_name, index_name=f"{table_name}_{column_name}_idx")

    # Test unique index creation with overridden index name
    column_name = "obj_order"
    create_index(table_name, column_name, f"{table_name}_unique_idx", index_op="unique")
    assert_index(db_metadata, table_name, column_name, index_name=f"{table_name}_unique_idx")

    # Test spatial index creation
    column_name = "test_geom"
    create_index(table_name, column_name, index_op="spatial")
    assert_index(db_metadata, table_name, column_name, index_name=f"{table_name}_{column_name}_spatial_idx")

    # Test json index creation (all ops)
    column_name = "test_json"
    create_index(table_name, column_name, index_op="json_full")
    assert_index(db_metadata, table_name, column_name, index_name=f"{table_name}_{column_name}_json_full_idx")

    # Test json index creation (path ops)
    column_name = "test_json"
    create_index(table_name, column_name, f"{table_name}_json_path_idx", index_op="json_path")
    assert_index(db_metadata, table_name, column_name, index_name=f"{table_name}_json_path_idx")

    # Test multi-column index creation on in-memory table

    # TSVECTOR indexes are not loaded from database via table reflection
    create_index(test_table, SEARCHABLE_COLS, f"{table_name}_search_idx", index_op="to_tsvector")
    assert_index(db_metadata, table_name, index_name=f"{table_name}_search_idx")

    # COALESCE indexes are not loaded from database via table reflection
    column_names = [c for c in SEARCHABLE_COLS if c.startswith("site")]
    index_cols = "_".join(col for col in column_names)
    index_name = f"{table_name}_{index_cols}_coalesce_idx"
    create_index(test_table, column_names, index_op="coalesce")
    assert_index(db_metadata, table_name, index_name=index_name)


def test_drop_index(db_metadata):
    table_name = SITE_TABLE_NAME
    test_table = db_metadata.tables[table_name]

    # Test with invalid parameters

    # Should raise no errors
    drop_index("nope", column_names="site_addr", ignore_errors=True)
    drop_index(table_name, ignore_errors=True)
    drop_index(table_name, index_name="nope", ignore_errors=True)

    with pytest.raises(ValueError, match="No table named"):
        drop_index("nope", column_names="site_addr", ignore_errors=False)
    with pytest.raises(ValueError, match="No index name provided"):
        drop_index(table_name, ignore_errors=False)
    with pytest.raises(Exception):
        drop_index(table_name, index_name="nope", ignore_errors=False)

    # Test removing APN index created during setup
    index_name = "order_index"
    drop_index(test_table, index_name, ignore_errors=False)
    assert_index(db_metadata, table_name, index_name=index_name, exists=False)

    # Test removing search index created during setup
    index_name = "tsvector_index"
    drop_index(table_name, index_name, ignore_errors=False)
    assert_index(db_metadata, table_name, index_name=index_name, exists=False)

    # Test removing indexes by column name

    pk_index = f"{table_name}_obj_index_obj_hash_idx"

    Index(pk_index, "pk", unique=True, _table=test_table).create()
    assert_index(db_metadata, table_name, index_name=pk_index)
    drop_index(table_name, column_names="obj_index,obj_hash", ignore_errors=False)
    assert_index(db_metadata, table_name, index_name=pk_index, exists=False)

    Index(pk_index, "pk", unique=True, _table=test_table).create()
    assert_index(db_metadata, table_name, index_name=pk_index)
    drop_index(table_name, column_names=["obj_index", "obj_hash"], ignore_errors=False)
    assert_index(db_metadata, table_name, index_name=pk_index, exists=False)


def test_has_index(db_metadata):
    table_name = SITE_TABLE_NAME
    test_table = db_metadata.tables[table_name]

    # Test indexes created during setup
    assert has_index(test_table, index_name="order_index")
    assert has_index(table_name, index_name="tsvector_index")

    # Test that indexes no longer exist after being dropped

    Index("order_index", _table=test_table).drop()
    Index("tsvector_index", _table=test_table).drop()

    assert not has_index(test_table, index_name="order_index")
    assert not has_index(table_name, index_name="tsvector_index")


def test_create_table(db_metadata):

    table_name = SITE_TABLE_NAME
    inject_sql = "DROP USER 'postgres' IF EXISTS"

    # Test with invalid parameters

    tmp_table_name = ALL_TEST_TABLES[2]

    # Test invalid table names
    with pytest.raises(ValueError, match="No table name specified"):
        create_table(None, col="string")
    with pytest.raises(ValueError, match="Invalid table name"):
        create_table(inject_sql, column_one="string")
    with pytest.raises(ValueError, match="Table already exists"):
        create_table(table_name, dropfirst=False, **SITE_COL_TYPES)
    # Test invalid index columns
    with pytest.raises(ValueError, match="No column names specified"):
        create_table("no_columns")
    with pytest.raises(ValueError, match="Invalid index column names"):
        create_table(tmp_table_name, index_cols="col,nope", col="string", dropfirst=True)
    with pytest.raises(ValueError, match="Invalid index column names"):
        create_table(tmp_table_name, index_cols=["col", "nope"], col="string", dropfirst=True)
    with pytest.raises(ValueError, match="Invalid index column names"):
        create_table(tmp_table_name, index_cols={"col": "unique", "nope": "unique"}, col="string", dropfirst=True)

    # Test with string of index columns

    create_table(
        table_name,
        index_cols="pk,obj_order",
        dropfirst=True,
        **SITE_COL_TYPES
    )
    assert_table(db_metadata, table_name, SITE_COL_TYPES)
    assert_index(db_metadata, table_name, index_name=f"{table_name}_pk_obj_order_idx")

    # Test with list of index columns

    refresh_metadata(db_metadata).tables[table_name].drop()

    create_table(
        table_name,
        index_cols=["pk", "obj_order"],
        dropfirst=False,
        **{k: v.__name__ for k, v in SITE_COL_TYPES.items()}
    )
    assert_table(db_metadata, table_name, SITE_COL_TYPES)
    assert_index(db_metadata, table_name, index_name=f"{table_name}_pk_idx")
    assert_index(db_metadata, table_name, index_name=f"{table_name}_obj_order_idx")

    # Test with dict of index columns and types

    refresh_metadata(db_metadata).tables[table_name].drop()

    create_table(
        table_name,
        index_cols={"pk": "unique", "obj_order": "unique", "pk,obj_order": "unique"},
        dropfirst=False,
        **{k: v() for k, v in SITE_COL_TYPES.items()}
    )
    assert_table(db_metadata, table_name, SITE_COL_TYPES)
    assert_index(db_metadata, table_name, index_name=f"{table_name}_pk_unique_idx")
    assert_index(db_metadata, table_name, index_name=f"{table_name}_obj_order_unique_idx")
    assert_index(db_metadata, table_name, index_name=f"{table_name}_pk_obj_order_unique_idx")


def test_drop_table(db_metadata):

    site_table = db_metadata.tables[SITE_TABLE_NAME]

    drop_table(SITE_TABLE_NAME)
    assert SITE_TABLE_NAME not in refresh_metadata(db_metadata).tables

    # Should raise no errors
    drop_table(site_table)
    drop_table(site_table.name)


def test_get_table(db_metadata):

    with pytest.raises(ValueError, match="No table named"):
        get_table("nope")

    # Test for existance of custom table
    assert get_table(SITE_TABLE_NAME).exists


def test_get_table_count(db_metadata):

    target_count = len(SITE_TEST_DATA)

    with pytest.raises(ValueError, match="No table named"):
        get_table_count("nope")

    # Test count for initialized data

    assert get_table_count(SITE_TABLE_NAME) == target_count
    assert get_table_count(db_metadata.tables[SITE_TABLE_NAME]) == target_count


def test_get_tables(db_metadata):

    all_tables = get_tables()
    table_name = SITE_TABLE_NAME

    # Test for existance of custom table
    assert table_name in all_tables
    assert all_tables[table_name].exists

    # Test for existance of tables specified as string

    some_tables = get_tables(f"{table_name},nope")

    assert len(some_tables) == 1
    assert table_name in some_tables
    assert some_tables[table_name].exists


def test_insert_from(db_metadata):

    from_table_name = SITE_TABLE_NAME
    into_table_name = ALL_TEST_TABLES[1]

    # Test with invalid parameters

    with pytest.raises(ValueError, match="No table named"):
        insert_from("nope", SITE_TABLE_NAME, "*")
    with pytest.raises(ValueError, match="No table named"):
        insert_from(from_table_name, "nope", "*")
    with pytest.raises(ValueError, match="Join columns missing in.*table"):
        insert_from(from_table_name, SITE_TABLE_NAME, "*", join_columns="nope")

    # Test with asterisk to insert all columns

    # Test that table is created with all columns if it doesn't exist
    insert_from(from_table_name, into_table_name, "*", create_if_not_exists=True)
    assert_table(db_metadata, into_table_name, SITE_TABLE_COLS)
    assert_records(db_metadata, into_table_name, SITE_DATA_DICT)

    # Test that table is updated with new records if it does
    insert_from(from_table_name, into_table_name, "*", create_if_not_exists=False)
    assert_records(db_metadata, into_table_name, SITE_DATA_DICT, target_count=(len(SITE_TEST_DATA) * 2))

    # Test with subset of columns

    target_columns = ("pk", "obj_order", "obj_hash", "site_zip")

    refresh_metadata(db_metadata).tables[into_table_name].drop()

    # Test that table is not created when only invalid column names are provided
    insert_from(from_table_name, into_table_name, "ignore,these", create_if_not_exists=True)
    assert into_table_name not in refresh_metadata(db_metadata).tables

    # Test that table is created with subset of columns if it doesn't exist
    insert_from(from_table_name, into_table_name, target_columns, create_if_not_exists=True)
    assert_table(db_metadata, into_table_name, target_columns)
    assert_records(db_metadata, into_table_name, SITE_DATA_DICT)

    # Test that table has no new records when only invalid column names are provided
    insert_from(from_table_name, into_table_name, "ignore,these")
    assert_table(db_metadata, into_table_name, target_columns)
    assert_records(db_metadata, into_table_name, SITE_DATA_DICT)

    # Test that existing table is updated with new records, ignoring two invalid columns
    target_count = len(SITE_DATA_DICT) * 2
    insert_from(from_table_name, into_table_name, target_columns + ("ignore", "these"))
    assert_records(db_metadata, into_table_name, SITE_DATA_DICT, target_count=target_count)

    # Test that table is not affected by duplicate records
    into_table = refresh_metadata(db_metadata).tables[into_table_name]
    target_count = select([func.count()]).select_from(into_table).scalar()
    insert_from(from_table_name, into_table_name, target_columns, join_columns=["pk", "obj_order", "obj_hash"])
    assert_records(db_metadata, into_table_name, SITE_DATA_DICT, target_count=target_count)


def test_insert_into(db_metadata):

    target_cols = ["pk", "str", "bool", "int"]
    into_table_name = ALL_TEST_TABLES[1]

    # Test with invalid parameters

    make_table(db_metadata, into_table_name, target_cols)

    with pytest.raises(ValueError, match="No table named"):
        insert_into("nope", [("one",), ("two",), ("three",)], "str")
    with pytest.raises(ValueError, match="Invalid column names"):
        insert_into(into_table_name, [("one",), ("two",), ("three",)], "no,nope,wrong")

    with pytest.raises(ValueError, match="Values provided do not match columns"):
        insert_into(into_table_name, [("one", "two"), ("three",), ("four",)], "str")
    with pytest.raises(ValueError, match="Values provided do not match columns"):
        insert_into(into_table_name, [("one",), ("two", "three"), ("four",)], "str")
    with pytest.raises(ValueError, match="Values provided do not match columns"):
        insert_into(into_table_name, ["one", ("two",), ("three", "four")], "str")

    # Test with empty values (logs warning and exits)
    insert_into(into_table_name, [], "str")

    # Cleanup in preparation for data tests
    refresh_metadata(db_metadata).tables[into_table_name].drop()

    # Prepare target data for insert

    target_vals = [
        {"pk": "128_2761_66", "str": "535 STATE ST", "bool": 1, "int": 42},
        {"pk": "128_2761_67", "str": "535 STATE ST", "bool": 0, "int": 86},
        {"pk": "128_2761_68", "str": "535 STATE ST", "bool": 1, "int": -4},
    ]
    target_data = {p["pk"]: p for p in target_vals}

    insert_vals = [
        # Ensure the order of values matches the target columns
        [p[c] for c in target_cols]
        for p in target_vals
    ]

    # Test insert with new table and no types specified

    insert_into(into_table_name, insert_vals, target_cols, create_if_not_exists=True)
    assert_table(db_metadata, into_table_name, target_cols)
    assert_records(db_metadata, into_table_name, target_data, target_cols)

    for inserted in refresh_metadata(db_metadata).tables[into_table_name].columns:
        assert str(inserted.type).lower() == "text"

    # Test insert duplicate records into existing table

    insert_into(into_table_name, insert_vals, target_cols)
    target_count = len(target_vals) * 2
    assert_table(db_metadata, into_table_name, target_cols)
    assert_records(db_metadata, into_table_name, target_data, target_cols, target_count)


def test_select_from(db_metadata):

    from_table_name = SITE_TABLE_NAME
    into_table_name = ALL_TEST_TABLES[1]

    # Test with invalid parameters

    with pytest.raises(ValueError, match="No table named"):
        select_from("nope", into_table_name, "*")
    with pytest.raises(ValueError, match="Table.*already exists"):
        select_from(from_table_name, SITE_TABLE_NAME, "*")

    # Test with invalid columns
    select_from(from_table_name, into_table_name, "ignore,these")
    assert into_table_name not in refresh_metadata(db_metadata).tables

    # Test with asterisk to insert all columns
    select_from(from_table_name, into_table_name, "*")
    assert_table(db_metadata, into_table_name, SITE_TABLE_COLS)
    assert_records(db_metadata, into_table_name, SITE_DATA_DICT)

    # Test with subset of columns (including two invalid)

    target_columns = ("pk", "obj_order", "obj_hash", "site_zip")

    refresh_metadata(db_metadata).tables[into_table_name].drop()

    select_from(from_table_name, into_table_name, target_columns + ("ignore", "these"))
    assert_table(db_metadata, into_table_name, target_columns)
    assert_records(db_metadata, into_table_name, SITE_DATA_DICT, target_columns=target_columns)


def test_select_into(db_metadata):

    into_table_name = ALL_TEST_TABLES[1]

    # Test with invalid parameters

    inject_sql = "DROP USER 'postgres' IF EXISTS"

    with pytest.raises(ValueError, match="Table.*already exists"):
        select_into(SITE_TABLE_NAME, [("one",), ("two",), ("three",)], "val")
    with pytest.raises(ValueError, match="No columns to select"):
        select_into(into_table_name, [("one",), ("two",), ("three",)], "")
    with pytest.raises(ValueError, match="Invalid column names"):
        select_into(into_table_name, [("one",), ("two",), ("three",)], inject_sql)
    with pytest.raises(ValueError, match="Column types provided do not match columns"):
        select_into(into_table_name, [("one",), ("two",), ("three",)], "val", "bool,json")

    with pytest.raises(ValueError, match="Values provided do not match columns"):
        select_into(into_table_name, [("one", "two"), ("three",), ("four",)], "val")
    with pytest.raises(ValueError, match="Values provided do not match columns"):
        select_into(into_table_name, [("one",), ("two", "three"), ("four",)], "val")
    with pytest.raises(ValueError, match="Values provided do not match columns"):
        select_into(into_table_name, ["one", ("two",), ("three", "four")], "val")

    # Test with empty values (logs warning and exits)
    select_into(into_table_name, [], "val")

    # Prepare target data for insert

    target_cols = SITE_TABLE_COLS
    target_data = {
        p["pk"]: {
            # Stringify JSON values for text comparison after insertion
            k: json.dumps(v) if "json" in k else v
            for k, v in p.items()
        }
        for p in SITE_TEST_DATA
    }
    insert_vals = [
        # Ensure the order of values matches the target columns
        [p[c] for c in target_cols]
        for p in target_data.values()
    ]
    insert_types = [
        # Use existing type dict to derive type names for each column
        SITE_COL_TYPES.get(col, sqltypes.Text).__visit_name__
        for col in target_cols
    ]

    # Test insert with no types specified (

    select_into(into_table_name, insert_vals, ",".join(target_cols))
    assert_table(db_metadata, into_table_name, target_cols)
    assert_records(db_metadata, into_table_name, target_data, target_cols)

    for inserted in refresh_metadata(db_metadata).tables[into_table_name].columns:
        assert str(inserted.type).lower() == "text"

    # Test insert with specific type names

    refresh_metadata(db_metadata).tables[into_table_name].drop()

    target_data = {p["pk"]: p for p in SITE_TEST_DATA}

    select_into(into_table_name, insert_vals, target_cols, insert_types)
    assert_table(db_metadata, into_table_name, target_cols)
    assert_records(db_metadata, into_table_name, target_data, target_cols)

    for idx, inserted in enumerate(refresh_metadata(db_metadata).tables[into_table_name].columns):
        assert str(inserted.type).lower() == insert_types[idx].lower()


def test_update_from(db_metadata):

    from_table_name = SITE_TABLE_NAME
    into_table_name = ALL_TEST_TABLES[1]

    # Test with invalid parameters

    with pytest.raises(ValueError, match="No table named"):
        update_from("nope", SITE_TABLE_NAME, "pk")
    with pytest.raises(ValueError, match="No table named"):
        update_from(from_table_name, "nope", "pk")
    with pytest.raises(ValueError, match="Join columns missing"):
        update_from(from_table_name, SITE_TABLE_NAME, "")
    with pytest.raises(ValueError, match="Join columns missing"):
        update_from(from_table_name, SITE_TABLE_NAME, ["site_addr", "nope"])

    # Create and populate a table with mangled data for testing updates

    orig_data = SITE_DATA_DICT
    join_cols = tuple(c for c in SITE_COL_TYPES if not c.startswith("test"))
    test_cols = tuple(SITE_COL_TYPES)
    test_data = {
        pk: {
            # Reverse string values for all but test columns
            k: v if k in test_cols else str(v)[::-1]
            for k, v in record.items()
        }
        for pk, record in orig_data.items()
    }

    make_table(db_metadata, into_table_name, SITE_TABLE_COLS, data=test_data)
    assert_table(db_metadata, into_table_name, SITE_TABLE_COLS)
    assert_records(db_metadata, into_table_name, test_data)

    # Test that all records are updated by join on target columns
    update_from(from_table_name, into_table_name, ",".join(join_cols))
    assert_records(db_metadata, into_table_name, orig_data)

    # Reset the updated table to mangled values for next test
    make_table(db_metadata, into_table_name, SITE_TABLE_COLS, data=test_data, dropfirst=False)
    assert_records(db_metadata, into_table_name, test_data)

    # Test that no records are updated when only invalid column names are provided
    update_from(from_table_name, into_table_name, join_cols, "ignore,these")
    assert_records(db_metadata, into_table_name, test_data)

    # Test that only select fields are updated by join on target columns, and invalid columns are ignored

    update_cols = set(c for c in SITE_TABLE_COLS if c.startswith("site"))
    ignore_cols = set(SITE_TABLE_COLS).difference(update_cols)

    update_from(from_table_name, into_table_name, join_cols, update_cols.union(("ignore", "these")))
    assert_records(db_metadata, into_table_name, orig_data, target_columns=update_cols)
    assert_records(db_metadata, into_table_name, test_data, target_columns=ignore_cols)


def test_update_rows(db_metadata):

    def update_zips(row):
        """
        Add integer zip to new column and json
        Row: pk, site_zip, size_zip_num, site_json
        """
        row = list(row)
        row[3]["zip"] = row[2] = int(row[1])
        return row

    def update_some(row):
        """
        Add "changed" key to JSON depending on address
        Row: pk, site_zip, size_zip_num, site_json
        """
        row = list(row)

        if row[3]["number"] != "7350":
            row = None
        else:
            row[3]["changed"] = True
        return row

    def update_none(row):
        return None

    test_table_name = ALL_TEST_TABLES[1]
    empty_table_name = ALL_TEST_TABLES[2]

    # Test with invalid parameters

    with pytest.raises(ValueError, match="No table named"):
        update_rows("nope", "pk", "site_addr", update_zips)
    with pytest.raises(ValueError, match="Join columns missing"):
        update_rows(SITE_TABLE_NAME, "", "site_addr", update_zips)
    with pytest.raises(ValueError, match="Target columns missing"):
        update_rows(SITE_TABLE_NAME, "pk", "", update_zips)
    with pytest.raises(ValueError, match="Invalid update function"):
        update_rows(SITE_TABLE_NAME, "pk", "site_addr", None, 0)
    with pytest.raises(ValueError, match="Invalid batch size"):
        update_rows(SITE_TABLE_NAME, "pk", "site_addr", update_zips, 0)

    with pytest.raises(ValueError, match="Join columns missing in.*table"):
        update_rows(SITE_TABLE_NAME, "pk,nope", "site_addr", update_zips)
    with pytest.raises(ValueError, match="Target columns missing in.*table"):
        update_rows(SITE_TABLE_NAME, "pk", ["site_addr", "nope"], update_zips)

    target_cols = ("site_zip", "site_zip_num", "site_json")

    # Test when there are no rows to update

    make_table(db_metadata, empty_table_name, SITE_TABLE_COLS)
    update_rows(empty_table_name, "pk", SITE_TABLE_COLS, update_zips)

    # Prepare a fully populated table

    # Insert test table columns in undefined order via `set`
    test_cols = list(set(SITE_TABLE_COLS).union(target_cols))[::-1]
    test_data = dict(SITE_DATA_DICT)
    # New table will have new column with numeric zip
    test_types = dict(SITE_COL_TYPES)
    test_types["site_zip_num"] = sqltypes.Integer

    # Create a test table with default data
    make_table(db_metadata, test_table_name, test_cols, test_types, data=test_data)
    assert_table(db_metadata, test_table_name, test_cols)
    assert_records(db_metadata, test_table_name, test_data)

    # Test updating all the rows in data table

    update_rows(test_table_name, "pk", target_cols, update_zips, batch_size=3)

    target_data = {}
    for pk, record in copy.deepcopy(test_data).items():
        parsed = int(record["site_zip"])
        record["site_zip_num"] = parsed
        record["site_json"]["zip"] = parsed
        target_data[pk] = record

    assert_records(db_metadata, test_table_name, target_data, target_cols)
    assert target_data != test_data
    assert f"tmp_{test_table_name}" not in refresh_metadata(db_metadata).tables

    # Test updating some the rows depending on address

    update_rows(test_table_name, "pk", target_cols, update_some, batch_size=3)

    test_data = target_data
    target_data = {}

    for pk, record in copy.deepcopy(test_data).items():
        if record["site_json"]["number"] == "7350":
            record["site_json"]["changed"] = True
        target_data[record["pk"]] = record

    assert_records(db_metadata, test_table_name, target_data, target_cols)
    assert target_data != test_data
    assert f"tmp_{test_table_name}" not in refresh_metadata(db_metadata).tables

    # Test updating none of the rows in the data table

    update_rows(test_table_name, "pk", target_cols, update_none, batch_size=3)

    assert_records(db_metadata, test_table_name, target_data, target_cols)
    assert f"tmp_{test_table_name}" not in refresh_metadata(db_metadata).tables


def test_table_exists(db_metadata):

    existing = db_metadata.tables

    # Test all tables present in database
    for table_name in existing:
        assert table_exists(existing.get(table_name))
        assert table_exists(table_name)

    assert not table_exists(None)
    assert not table_exists("nope")


def test_create_foreign_key(db_metadata):

    site_table = db_metadata.tables[SITE_TABLE_NAME]
    test_table_name = ALL_TEST_TABLES[1]

    # Test with invalid parameters

    with pytest.raises(ValueError, match="No table named"):
        create_foreign_key("nope", "pk", f"{site_table.name}.obj_order")
    with pytest.raises(ValueError, match="Invalid column names"):
        create_foreign_key(site_table.name, "nope", f"{site_table.name}.obj_order")
    with pytest.raises(ValueError, match="No related column named"):
        create_foreign_key(site_table.name, "pk", f"{site_table.name}.nope")

    test_columns = ("pk", "obj_order", "obj_hash", "test_bool")

    # Create an empty test table to link with a foreign key
    test_table = make_table(db_metadata, test_table_name, test_columns)
    assert_table(db_metadata, test_table.name, test_columns)

    # Ensure there are no foreign keys before the operation
    assert len(refresh_metadata(db_metadata).tables[test_table_name].foreign_keys) == 0

    # Test FK creation when a table name is passed in with a column string
    create_foreign_key(test_table_name, "pk", f"{site_table.name}.pk")
    test_table = refresh_metadata(db_metadata).tables[test_table_name]
    assert len(test_table.foreign_keys) == 1
    assert len(test_table.columns.pk.foreign_keys) == 1

    # Test FK creation when a table is passed in with a column object
    create_foreign_key(test_table, "obj_order", site_table.columns.obj_order)
    test_table = refresh_metadata(db_metadata).tables[test_table_name]
    assert len(test_table.foreign_keys) == 2
    assert len(test_table.columns.obj_order.foreign_keys) == 1


def test_drop_foreign_key(db_metadata):

    site_table = db_metadata.tables[SITE_TABLE_NAME]
    test_table_name = ALL_TEST_TABLES[1]

    # Test with invalid parameters

    with pytest.raises(ValueError, match="No table named"):
        drop_foreign_key("nope", "pk")
    with pytest.raises(ValueError, match="No such foreign key in table"):
        drop_foreign_key(site_table.name, "nope")

    test_columns = ("pk", "obj_order", "obj_hash")

    # Create an empty test table to link with foreign keys

    test_table = make_table(db_metadata, test_table_name, test_columns)
    assert_table(db_metadata, test_table.name, test_columns)

    fk1 = ForeignKeyConstraint(
        columns=[test_table.columns.pk],
        refcolumns=[site_table.columns.pk],
        name="test_table_first_fkey",
    )
    ddl = AddConstraint(fk1)
    ddl.execute(test_table.bind, ddl.target)

    fk2 = ForeignKeyConstraint(
        columns=[test_table.columns.obj_order],
        refcolumns=[site_table.columns.obj_order],
        name="test_table_next_fkey",
    )
    ddl = AddConstraint(fk2)
    ddl.execute(test_table.bind, ddl.target)

    fk3 = ForeignKeyConstraint(
        columns=[test_table.columns.obj_hash],
        refcolumns=[site_table.columns.obj_hash],
        name="test_table_last_fkey"
    )
    ddl = AddConstraint(fk3)
    ddl.execute(test_table.bind, ddl.target)

    test_table = refresh_metadata(db_metadata).tables[test_table_name]
    assert len(test_table.foreign_keys) == 3
    assert len(test_table.columns.pk.foreign_keys) == 1
    assert len(test_table.columns.obj_order.foreign_keys) == 1
    assert len(test_table.columns.obj_hash.foreign_keys) == 1

    # Test FK deletion when a table name is passed in with a mixed-case FK name
    drop_foreign_key(test_table_name, "test_table_FIRST_fkey")
    test_table = refresh_metadata(db_metadata).tables[test_table_name]
    assert len(test_table.foreign_keys) == 2
    assert len(test_table.columns.pk.foreign_keys) == 0
    assert len(test_table.columns.obj_order.foreign_keys) == 1
    assert len(test_table.columns.obj_hash.foreign_keys) == 1

    # Test FK deletion when a table object is passed in with an FK constraint
    drop_foreign_key(test_table, fk2)
    test_table = refresh_metadata(db_metadata).tables[test_table_name]
    assert len(test_table.foreign_keys) == 1
    assert len(test_table.columns.pk.foreign_keys) == 0
    assert len(test_table.columns.obj_order.foreign_keys) == 0
    assert len(test_table.columns.obj_hash.foreign_keys) == 1

    # Test FK deletion when a table object is passed in with an FK object
    drop_foreign_key(test_table, fk3.elements[0])
    test_table = refresh_metadata(db_metadata).tables[test_table_name]
    assert len(test_table.foreign_keys) == 0
    assert len(test_table.columns.pk.foreign_keys) == 0
    assert len(test_table.columns.obj_order.foreign_keys) == 0
    assert len(test_table.columns.obj_hash.foreign_keys) == 0


def test_alter_column_type(db_metadata):

    table_name = SITE_TABLE_NAME
    inject_sql = "DROP USER 'postgres' IF EXISTS"

    # Test SQL injection code
    with pytest.raises(ValueError, match="Invalid table name"):
        alter_column_type(inject_sql, "test_bool", "int")
    with pytest.raises(ValueError, match="Invalid column name"):
        alter_column_type(table_name, inject_sql, "int")
    with pytest.raises(ValueError, match="Invalid column type"):
        alter_column_type(table_name, "test_bool", inject_sql)

    # PK column tests

    # Ensure original column is type INTEGER
    original = db_metadata.tables.get(table_name).columns.pk
    assert str(original.type).lower() == "integer"

    # Test change from INTEGER to VARCHAR
    alter_column_type(table_name, "pk", "varchar")
    altered = refresh_metadata(db_metadata).tables.get(table_name).columns.pk
    assert str(altered.type).lower() == "varchar"

    # Test change from VARCHAR back to INTEGER
    alter_column_type(table_name, "pk", "int")
    altered = refresh_metadata(db_metadata).tables.get(table_name).columns.pk
    assert str(altered.type).lower() == "integer"

    # Bool column tests

    # Ensure original column is type BOOLEAN
    original = db_metadata.tables.get(table_name).columns.test_bool
    assert str(original.type).lower() == "boolean"

    # Test change from BOOLEAN to INTEGER
    alter_column_type(db_metadata.tables[table_name], "test_bool", "int")
    altered = refresh_metadata(db_metadata).tables.get(table_name).columns.test_bool
    assert str(altered.type).lower() == "integer"

    # Test change from INTEGER back to BOOLEAN
    alter_column_type(db_metadata.tables[table_name], "test_bool", "bool")
    altered = refresh_metadata(db_metadata).tables.get(table_name).columns.test_bool
    assert str(altered.type).lower() == "boolean"


def test_create_column(db_metadata):

    site_table = db_metadata.tables[SITE_TABLE_NAME]
    inject_sql = "DROP USER 'postgres' IF EXISTS"

    # Test SQL injection code
    with pytest.raises(ValueError, match="Invalid table name"):
        create_column(inject_sql, "test_json", "jsonb", default="")
    with pytest.raises(ValueError, match="Invalid column name"):
        create_column(site_table.name, inject_sql, "jsonb", default="")
    with pytest.raises(ValueError, match="Invalid column type"):
        create_column(site_table, "test_json", inject_sql, default="")
    with pytest.raises(ValueError, match="Invalid default value"):
        create_column(site_table.name, "test_json", "jsonb", default=inject_sql)

    # Test when column already exists

    column = "test_bool"
    assert column in site_table.columns

    create_column(site_table.name, "test_bool", "bool", default=False, checkfirst=True)
    with pytest.raises(Exception):
        create_column(site_table.name, "test_bool", "bool", default=False, checkfirst=False)

    # Test column creation

    column = "test_text"
    create_column(site_table.name, column, "varchar", default="nothing")
    newcol = refresh_metadata(db_metadata).tables[site_table.name].columns.get(column)
    assert column == newcol.name
    assert str(newcol.type).lower().startswith("varchar")
    assert not newcol.nullable

    column = "test_true"
    create_column(site_table.name, column, "bool", default=True)
    newcol = refresh_metadata(db_metadata).tables[site_table.name].columns.get(column)
    assert column == newcol.name
    assert str(newcol.type).lower().startswith("bool")
    assert not newcol.nullable

    column = "test_int"
    create_column(site_table.name, column, "integer", default=50)
    newcol = refresh_metadata(db_metadata).tables[site_table.name].columns.get(column)
    assert column == newcol.name
    assert str(newcol.type).lower().startswith("integer")
    assert not newcol.nullable

    column = "test_num"
    create_column(site_table.name, column, "decimal", default=3.14159)
    newcol = refresh_metadata(db_metadata).tables[site_table.name].columns.get(column)
    assert column == newcol.name
    assert str(newcol.type).lower().startswith("numeric")
    assert not newcol.nullable

    column = "test_jsonb"
    create_column(site_table.name, column, "jsonb", nullable=True)
    newcol = refresh_metadata(db_metadata).tables[site_table.name].columns.get(column)
    assert column == newcol.name
    assert str(newcol.type).lower().startswith("json")
    assert newcol.nullable


def test_drop_column(db_metadata):

    site_table = db_metadata.tables[SITE_TABLE_NAME]
    inject_sql = "DROP USER 'postgres' IF EXISTS"

    # Test SQL injection code
    with pytest.raises(ValueError, match="Invalid table name"):
        drop_column(inject_sql, "test_bool")
    with pytest.raises(ValueError, match="Invalid column name"):
        drop_column(site_table.name, inject_sql)

    # Test when the column doesn't exist

    column = "nope"
    assert column not in site_table.columns
    drop_column(site_table.name, column, checkfirst=True)
    assert column not in refresh_metadata(db_metadata).tables[site_table.name].columns

    # Test for the presence and removal of a simple column

    column = "test_bool"
    assert column in site_table.columns
    drop_column(site_table.name, column)
    assert column not in refresh_metadata(db_metadata).tables[site_table.name].columns

    # Test for the presence and removal of an indexed column

    column = "obj_order"
    assert column in site_table.columns
    drop_column(site_table, column)
    assert column not in refresh_metadata(db_metadata).tables[site_table.name].columns


def test_create_tsvector_column(db_metadata):
    """ Intentionally not covered since it contains a sqlalchemy workaround """

    site_table = db_metadata.tables[SITE_TABLE_NAME]
    inject_sql = "DROP USER 'postgres' IF EXISTS"

    # At least test SQL injection code
    with pytest.raises(ValueError, match="Invalid table name"):
        create_tsvector_column(inject_sql, "searchable", ["obj_hash"])
    with pytest.raises(ValueError, match="Invalid column name"):
        create_tsvector_column(site_table, inject_sql, ["obj_hash"], "tsvector_index")
    with pytest.raises(ValueError, match="Invalid column names"):
        create_tsvector_column(site_table.name, "searchable", ["obj_hash", inject_sql], "tsvector_index")

    # Test when column already exists

    with pytest.raises(Exception):
        create_tsvector_column(site_table.name, "site_addr", SEARCHABLE_COLS)

    # Test column creation (unable tests remotely: requires PostgreSQL 12)

    # col_name = "generated_search_col"
    # idx_name = "generated_tsvector_index"
    # create_tsvector_column(site_table.name, col_name, SEARCHABLE_COLS, index_name=idx_name)
    #
    # newcol = refresh_metadata(db_metadata).tables[site_table.name].columns.get(col_name)
    # assert col_name == newcol.name
    # assert str(newcol.type).lower().startswith("tsvector")
    #
    # # TSVECTOR indexes are not loaded from database via table reflection
    # assert_index(db_metadata, site_table.name, index_name=idx_name)


def test_query_json_keys(db_metadata):

    site_table = db_metadata.tables[SITE_TABLE_NAME]

    # Test with invalid parameters

    with pytest.raises(ValueError, match="No table named"):
        query_json_keys("nope", "site_addr", {"state": "NY"})
    with pytest.raises(ValueError, match="Invalid column name"):
        query_json_keys(SITE_TABLE_NAME, "nope", {"state": "NY"})

    # Test a query that will return all columns for all records
    limit = len(SITE_TEST_DATA)
    search_results = query_json_keys(site_table, "site_json", {"city": "ALBANY", "state": "NY"})
    assert limit == len({result["pk"] for result in search_results})
    assert all(len(result) == len(SITE_TABLE_COLS) for result in search_results)

    # Test limiting a query that will return all columns for all records
    limit = round(len(SITE_TEST_DATA) / 2)
    search_results = query_json_keys(site_table, "site_json", {"city": "ALBANY", "state": "NY"}, limit=limit)
    assert limit == len({result["pk"] for result in search_results})
    assert all(len(result) == len(SITE_TABLE_COLS) for result in search_results)

    # Test an excessive limit on a query that will return all columns for all records
    limit = len(SITE_TEST_DATA)
    search_results = query_json_keys(site_table, "site_json", {"city": "ALBANY", "state": "NY"}, limit=(limit * 2))
    assert limit == len({result["pk"] for result in search_results})
    assert all(len(result) == len(SITE_TABLE_COLS) for result in search_results)

    # Test a single matching address as string
    query, matches = json.dumps({"number": "7550", "street": "STATE ST STE CML5"}), 1
    search_results = query_json_keys(site_table.name, "site_json", query)
    assert matches == len({result["pk"] for result in search_results})

    # Test an invalid address
    query, matches = {"street": "nope"}, 0
    search_results = query_json_keys(site_table.name, "site_json", query)
    assert matches == len({result["pk"] for result in search_results})

    # Test an empty address
    query, matches = '""', 0
    search_results = query_json_keys(site_table.name, "site_json", query)
    assert matches == len({result["pk"] for result in search_results})


def test_query_tsvector_columns(db_metadata):

    site_table = db_metadata.tables[SITE_TABLE_NAME]

    # Test with invalid parameters

    with pytest.raises(ValueError, match="No table named"):
        query_tsvector_columns("nope", "site_addr", "NY")
    with pytest.raises(ValueError, match="Invalid column names"):
        query_tsvector_columns(site_table, "nope", "NY")

    # Test queries that match all records
    limit = len(SITE_TEST_DATA)
    for query in ("ALBANY", "NY", "STATE", "12224"):
        assert limit == len(query_tsvector_columns(SITE_TABLE_NAME, SEARCHABLE_COLS, query))

    # Test that limit applies to queries matching all records
    for limit, query in enumerate(("ALBANY", "NY", "STATE", "12224")):
        search_results = query_tsvector_columns(site_table, SEARCHABLE_COLS, query, limit=limit)
        assert limit == len({result["pk"] for result in search_results})

    # Test an excessive limit on a query that matches all records
    query, matches = "NY", len(SITE_TEST_DATA)
    search_results = query_tsvector_columns(site_table.name, SEARCHABLE_COLS, query, limit=(matches * 2))
    assert matches == len({result["pk"] for result in search_results})
    assert all(len(result) == len(SITE_TABLE_COLS) for result in search_results)

    # Test queries that match a single record

    query, matches = "0-0-7350-12224", 1
    search_results = query_tsvector_columns(site_table.name, SEARCHABLE_COLS, query)
    assert matches == len({result["pk"] for result in search_results})
    assert all(len(result) == len(SITE_TABLE_COLS) for result in search_results)

    query, matches = "7550 STATE ST STE CML5", 1
    search_results = query_tsvector_columns(site_table.name, SEARCHABLE_COLS, query)
    assert matches == len({result["pk"] for result in search_results})
    assert all(len(result) == len(SITE_TABLE_COLS) for result in search_results)

    terms = "7550 STATE ST STE CML5".split()[::-1]
    query, matches = " ".join(terms), 1
    search_results = query_tsvector_columns(site_table.name, SEARCHABLE_COLS, query)
    assert matches == len({result["pk"] for result in search_results})
    assert all(len(result) == len(SITE_TABLE_COLS) for result in search_results)

    query, matches = "8-4-7550-12224 7550 STATE ST STE CML5 ALBANY NY 12224", 1
    search_results = query_tsvector_columns(site_table.name, SEARCHABLE_COLS, query)
    assert matches == len({result["pk"] for result in search_results})
    assert all(len(result) == len(SITE_TABLE_COLS) for result in search_results)

    terms = "8-4-7550-12224 7550 STATE ST STE CML5 ALBANY NY 12224".split()[::-1]
    query, matches = " ".join(terms), 1
    search_results = query_tsvector_columns(site_table.name, SEARCHABLE_COLS, query)
    assert matches == len({result["pk"] for result in search_results})
    assert all(len(result) == len(SITE_TABLE_COLS) for result in search_results)

    # Test queries that don't match any records

    query, matches = "nope", 0
    search_results = query_tsvector_columns(site_table.name, SEARCHABLE_COLS, query)
    assert matches == len({result["pk"] for result in search_results})

    query, matches = "STATE ST", 0
    search_results = query_tsvector_columns(site_table.name, "obj_hash", query)
    assert matches == len({result["pk"] for result in search_results})

    query, matches = "0-0-7350-12224", 0
    search_results = query_tsvector_columns(site_table.name, "site_addr", query)
    assert matches == len({result["pk"] for result in search_results})
