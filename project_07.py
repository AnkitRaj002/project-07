import random
sentence_starter = ['Long long ago' , 'Once upon a time' , 'The date was 13th july' , 'A few Days ago' , 'since 20 years']
character = [' there lived a man named Sundar Rajan.' , ' there lived a farmer.' , ' a blind man.' , ' a mischevious boy named Rahul.' , ' there lived a king.']
time=[' one day' , ' one one fine morning' , ' in the dark night' , ' in the evening' , ' in the after noon' ,]
story_plot = [' he was passing by' , ' he was going to play cricket' ,' he is going to fields' , ' he is going to home from work' , ' he is going to school']
second_character = [' he saw a man' , ' he saw a woman' , ' he saw a shadow of a woman' , ' he saw a old man who is unable to walk']
work  = [' he is dugging a well.', ' searching something', ' waiting for his friend', ' saw something suspiseous']
print(random.choice(sentence_starter)+random.choice(character)+random.choice(time)+random.choice(story_plot)+random.choice(second_character)+random.choice(work))