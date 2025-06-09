class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # supplies를 hashmap에 넣고.. 문제는 recipe가 ingredients에 들어갈 수 있다는 점
        # topological sort로 recipe끼리 관계를 정리하면 풀 수 있을 듯?
        recipes_set = set(recipes)
        supplies_set = set(supplies)
        recipe_to_ingredient = {}

        graph, in_degree = {}, {}
        for i in range(len(recipes)):
            graph[recipes[i]] = []
            in_degree[recipes[i]] = 0
            recipe_to_ingredient[recipes[i]] = ingredients[i]

        for recipe, ingredient_list in zip(recipes, ingredients):
            for base_recipe in ingredient_list:
                if base_recipe in recipes_set:
                    graph[base_recipe].append(recipe)
                    in_degree[recipe] += 1

        q = collections.deque()
        for recipe in in_degree:
            if in_degree[recipe] == 0:
                q.append(recipe)

        res = []
        while q:
            recipe = q.popleft()
            
            can_make_recipe = True
            for ingredient in recipe_to_ingredient[recipe]:
                if ingredient in recipes_set:
                    continue
                if ingredient not in supplies_set:
                    can_make_recipe = False
                    break
            
            if not can_make_recipe:
                continue
            
            res.append(recipe)
            for next_recipe in graph[recipe]:
                in_degree[next_recipe] -= 1
                if in_degree[next_recipe] == 0:
                    q.append(next_recipe)

        return res
