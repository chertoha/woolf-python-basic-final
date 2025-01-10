from typing import List
from src.decorators.catch import catch
from src.decorators.confirm import confirm


@catch
@confirm("Ви впевнені, що хочете видалити ці теги?")
def remove_tags(args: List[str]):
    print("remove_tags")
