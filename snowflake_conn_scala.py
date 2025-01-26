import os
import snowflake.connector as sc

private_key_file = '<path>'
private_key_file_pwd = '<password>'

conn_params = {
    'account': '<account_identifier>',
    'user': '<user>',
    'private_key_file': private_key_file,
    'private_key_file_pwd':private_key_file_pwd,
    'warehouse': '<warehouse>',
    'database': '<database>',
    'schema': '<schema>'
}

ctx = sc.connect(**conn_params)
cs = ctx.cursor()