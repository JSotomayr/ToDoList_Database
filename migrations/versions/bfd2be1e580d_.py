"""empty message

Revision ID: bfd2be1e580d
Revises: a81ab20ba7e0
Create Date: 2021-11-15 11:41:54.422158

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'bfd2be1e580d'
down_revision = 'a81ab20ba7e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_constraint('task_ibfk_1', 'task', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('task_ibfk_1', 'task', 'user', ['user_id'], ['id'])
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nick', mysql.VARCHAR(length=120), nullable=False),
    sa.Column('_is_active', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False),
    sa.CheckConstraint('(`_is_active` in (0,1))', name='user_chk_3'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
