# Habilita PyMySQL como reemplazo de MySQLdb
import pymysql
pymysql.version_info = (2, 2, 8, "final", 0)
pymysql.install_as_MySQLdb()