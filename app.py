from  data_creator import RetrieveSearchData

# Men - 'diet'
men_diet = RetrieveSearchData('men', 'diet')
men_diet_data = men_diet.get_search_data()
men_diet_results = men_diet.get_word_counts(men_diet_data)

# Women - 'diet'
women_diet = RetrieveSearchData('women', 'diet')
women_diet_data = women_diet.get_search_data()
women_diet_results = women_diet.get_word_counts(women_diet_data)

# Show data
men_diet_results.plot(10)
women_diet_results.plot(10)
plt.show()
