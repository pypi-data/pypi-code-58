"""empty message

Revision ID: 4f2398ebcd49
Revises: 389cfb9de776
Create Date: 2019-02-15 18:22:51.684630

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4f2398ebcd49'
down_revision = '389cfb9de776'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('search_filter', sa.Column('entity_type', sa.String(length=80)))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('search_filter', 'entity_type')
    # ### end Alembic commands ###
