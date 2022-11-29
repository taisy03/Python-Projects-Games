import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('averaged_perceptron_tagger')
#For name, I only used the numeric string which tests wether the input is numeric.
#IMPROVE : it still passes if it had numbers and letters e.g 23sdf (try to fix this)
while True :
      female_name = input("Female name:")
      if female_name.isnumeric() :
            print("That\'s not a name!")
      else:
            break 

#for adjectives, i first check if its in other forms e.g (bigger /biggest) and then check if its an adjective
while True :
      adj1 = input("Adjective:")
      valjj = nltk.pos_tag([adj1])
      ansjj = valjj[0][1] 
      if(ansjj == 'JJR' or ansjj == 'JJS') :
            print("That\'s the wrong form , sorry I should have specified!")     
      elif(ansjj != 'JJ') :
            print("That\'s not an adjective!")
      else:
            break
#for nouns I check if its a noun , and wether its a plural noun.
while True :
      plural_noun = input("Plural noun:")
      val1 = nltk.pos_tag([plural_noun])
      ans1 = val1[0][1] 
      if(ans1 != 'NN' and ans1 != 'NNS'):
            print("That\'s not a noun!")
      elif(ans1 != 'NNS' and ans1 == 'NN'):
            print("That\'s not a plural noun!")
      else:
            break

while True : 
      verb1 = input("Verb:")
      valverb = nltk.pos_tag([verb1])
      ansverb = valverb[0][1]
      if(ansverb != 'VB') :
            print("That\'s not a verb!")
      else:
            break

while True :    
      noun1 = input("Noun:")
      val2 = nltk.pos_tag([noun1])
      ans2 = val2[0][1] 
      if(ans2 == 'NNS') :
            print("That\'s a plural noun!")
      
      elif(ans2 != 'NN'):
            print("That\'s not a noun!")
      else:
            break

while True : 
      colour = input("Colour:")
      if colour.isnumeric():
            print("That\'s not a colour!")
      else:
            break

while True : 
      adj2 = input("Adjective:")
      valjj2 = nltk.pos_tag([adj2])
      ansjj2 = valjj2[0][1] 
      if(ansjj2 == 'JJR' or ansjj2 == 'JJS') :
            print("That\'s the wrong form , sorry I should have specified!")
      
      elif(ansjj2 != 'JJ') :
            print("That\'s not an adjective!")
      else:
            break

while True :    
      animal = input("Animal:")
      if animal.isnumeric() :
            print("That\'s not an animal!")
      else:
            break

while True : 
      noun2 = input("Noun:")
      val3 = nltk.pos_tag([noun2])
      ans3 = val3[0][1] 
      if(ans3 == 'NNS') :
            print("That\'s a plural noun!")
      
      elif(ans3 != 'NN'):
            print("That\'s not a noun!")
      else:
            break

while True : 
      body_part = input("Body part:")
      if body_part.isnumeric():
            print("That\'s not a body part!")
      else:
            break

while True :
      verb2 = input("Verb:")
      valverb2 = nltk.pos_tag([verb2])
      ansverb2 = valverb2[0][1]
      if(ansverb2 != 'VB') :
            print("That\'s not a verb!")
      else:
            break

print (f"{female_name} was being chased down the street by two {adj1} {plural_noun}. She was starting to get out of breath so she decided to {verb1} a {noun1}. \
Somehow, that worked! They stopped chasing her. But now she had an even bigger \
problem. Out of nowhere, a {colour} {adj2} {animal} appeared. She saw a {noun2} near her and hit the {animal} in the {body_part}. But that did not work.\
The {animal} started to {verb2} so {female_name} had to {verb2} too! What a wierd story.")

