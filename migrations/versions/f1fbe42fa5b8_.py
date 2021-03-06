"""empty message

Revision ID: f1fbe42fa5b8
Revises: 9022edd26a32
Create Date: 2022-06-22 16:59:27.870943

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1fbe42fa5b8'
down_revision = '9022edd26a32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pokemon', 'moves')
    op.drop_column('pokemon', 'types')
    op.drop_column('pokemon', 'abilities')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon', sa.Column('abilities', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('pokemon', sa.Column('types', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.add_column('pokemon', sa.Column('moves', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
