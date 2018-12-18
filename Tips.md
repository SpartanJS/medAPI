#Tips v 0.0.1

#1  Changing Database  (ie : DB Corrupted):
- Creating a new db in postgres > CREATE DATABASE new_db_name
- Modifying the CONFIG file > dbname = 'new_db_name'
- Renaming the /migration folder > /migration_old_db_name
- Reinitialize the SQLAlchemy objects > python manage.py db initial
- Do as usual > Migrate > Upgrate
- Enjoy

#2 Linking 2 tables with a couple of foreign key(=composite key)
- Use db.ForeignKeyConstraint( [FK1, FK2],[other_table.FK1, other_table.FK2])
- Use primaryjoin in db.relationship(...primaryjoin="(table.FK1==other_table.FK1)&(table...)")
