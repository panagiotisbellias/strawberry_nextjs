import strawberry

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

authors = []

@strawberry.type
class Query:
    @strawberry.field
    def all_authors(self) -> list[str]:
        return authors

@strawberry.type
class Mutation:
    @strawberry.field
    def add_author(self, name: str) -> list[str]:
        authors.append(name)
        return name

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")