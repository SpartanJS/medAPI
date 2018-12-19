"""empty message

Revision ID: e24bf24f17f9
Revises: 5790f8d1b552
Create Date: 2018-12-18 12:53:56.964693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e24bf24f17f9'
down_revision = '5790f8d1b552'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('surveysquestionstable', sa.Column('qa_id', sa.String(), nullable=False))
    op.add_column('surveysquestionstable', sa.Column('sa_id', sa.String(), nullable=False))
    op.drop_constraint('surveysquestionstable_s_id_fkey', 'surveysquestionstable', type_='foreignkey')
    op.drop_constraint('surveysquestionstable_q_id_fkey', 'surveysquestionstable', type_='foreignkey')
    op.create_foreign_key(None, 'surveysquestionstable', 'questionstable', ['qa_id'], ['q_id'])
    op.create_foreign_key(None, 'surveysquestionstable', 'surveystable', ['sa_id'], ['s_id'])
    op.drop_column('surveysquestionstable', 'q_id')
    op.drop_column('surveysquestionstable', 's_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('surveysquestionstable', sa.Column('s_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('surveysquestionstable', sa.Column('q_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'surveysquestionstable', type_='foreignkey')
    op.drop_constraint(None, 'surveysquestionstable', type_='foreignkey')
    op.create_foreign_key('surveysquestionstable_q_id_fkey', 'surveysquestionstable', 'questionstable', ['q_id'], ['q_id'])
    op.create_foreign_key('surveysquestionstable_s_id_fkey', 'surveysquestionstable', 'surveystable', ['s_id'], ['s_id'])
    op.drop_column('surveysquestionstable', 'sa_id')
    op.drop_column('surveysquestionstable', 'qa_id')
    # ### end Alembic commands ###