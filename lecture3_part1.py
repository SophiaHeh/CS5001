'''
create some lists and explores some of their functions
'''
list_movies = ["hangover", "interstellar",
               "the prestige", "catch me if you can"]
print(list_movies)
print(f"The length of list_movie is {len(list_movies)}")
# Append allows me to add an item to the end of list (add on the last position)
list_movies.append("harry potter")
# print(list_movies)

# use insert method to "specify what location" you want to insert
list_movies.insert(2, "harry potter")
# print(list_movies)


# use remove method to remove a particular element #remove() 是用來從列表中移除“第一個”匹配的元素的函數，若元素不在列表中，則會拋出錯誤。
list_movies.remove("harry potter")

# delete second "harry potter" only
new_list = list_movies[0: len(list_movies)-1]
print(list_movies)
print(new_list)

# pop() 用於根據索引移除列表中的元素，並“返回”被移除的值。當不指定索引時，它會默認移除最後一個元素。需要新變量來承接返回的值
# pop()和remove()不一樣，remove()是不會返回數值的，所以不用賦予新變量。 https://chatgpt.com/share/6712c60f-4af0-8001-b8a7-8e100640d82d
