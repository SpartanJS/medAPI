"""empty message

Revision ID: bf35e36947ae
Revises: 
Create Date: 2018-12-14 20:12:47.959431

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf35e36947ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('responsestable',
    sa.Column('r_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('r_admin', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('r_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('responsestable')
    # ### end Alembic commands ###