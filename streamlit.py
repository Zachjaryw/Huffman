##################################################################################
#  In order to run this program, go into Terminal and type
# "streamlit run /Users/Zach/Documents/streamlit.py --server.maxUploadSize = 1028".
# After a few seconds a webpage should open with the user
# friendly version of the program.
##################################################################################

import pandas as pd
import numpy as np
import streamlit as st
import random


def huffman_index(string):
  breakdown = list(string)
        
  x = 0
  letters = []
  appear = []
  while x != len(breakdown):
      if breakdown[x] in letters:
          appear[letters.index(breakdown[x])] += 1
      else:
          letters.append(breakdown[x])
          appear.append(1)
      x += 1
  combine = pd.DataFrame(
      {
          'letters':letters,
          'appear':appear
          }
      )
  combine = combine.sort_values('appear', ascending = False)

  appear_to_drop = combine['appear'].values.tolist()
  letters_to_drop = combine['letters'].values.tolist()
  number = []
  hold_values = []
  left = []
  right = []
  combo_l = ''
  combo_a = 0
  y = len(letters_to_drop); z = 0
  num = int(len(breakdown))  

  while len(letters_to_drop) != 3:
      number.append(appear_to_drop[-1] + appear_to_drop[-2])
      left.append(letters_to_drop[-1])
      right.append(letters_to_drop[-2])
      combo_l = letters_to_drop[-1] + letters_to_drop[-2]
      combo_a = number[-1]
      letters_to_drop.remove(letters_to_drop[-1])
      letters_to_drop.remove(letters_to_drop[-1])
      letters_to_drop.append(combo_l)
      appear_to_drop.remove(appear_to_drop[-1])
      appear_to_drop.remove(appear_to_drop[-1])
      appear_to_drop.append(combo_a)
      combine_b = pd.DataFrame(
          {
              'letters':letters_to_drop,
              'appear':appear_to_drop
              }
          )
      combine_b = combine_b.sort_values('appear', ascending = False)
      appear_to_drop = combine_b['appear'].values.tolist()
      letters_to_drop = combine_b['letters'].values.tolist()
      y = len(letters_to_drop)

      z = z+1



  left.append(letters_to_drop[-1])
  right.append(letters_to_drop[-2])
  letters_to_drop.remove(letters_to_drop[-1])
  letters_to_drop.remove(letters_to_drop[-1])
  appear_to_drop.remove(appear_to_drop[-1])
  appear_to_drop.remove(appear_to_drop[-1])

  if len(letters_to_drop) == 1:
      left.append(letters_to_drop[-1])
      right.append(left[-2] + right[-1])
      letters_to_drop.remove(letters_to_drop[-1])
      appear_to_drop.remove(appear_to_drop[-1])
  else:
      pass

  left_flip = pd.DataFrame(left)
  left_flip = left_flip.reset_index()
  left_flip = left_flip.sort_values('index',ascending = False)
  left_flip.columns = ['index','left']
  left = left_flip['left'].values.tolist()
  right_flip = pd.DataFrame(right)
  right_flip = right_flip.reset_index()
  right_flip = right_flip.sort_values('index',ascending = False)
  right_flip.columns = ['index','right']
  right = right_flip['right'].values.tolist()

  encoder_index = pd.DataFrame(
      {
        'left': left,
        'right': right
      }
  )
  encoder_index = encoder_index.reset_index()
  encoder_index = encoder_index.sort_values('index',ascending = True)
  encoder_index = encoder_index.set_index('index')
  encoder_index = encoder_index.reset_index(drop = True)
  #print(encoder_index)
  return encoder_index

def huffman_encrypt(string):
  breakdown = list(string)
  x = 0
  letters = []
  appear = []
  while x != len(breakdown):
      if breakdown[x] in letters:
          appear[letters.index(breakdown[x])] += 1
      else:
          letters.append(breakdown[x])
          appear.append(1)
      x += 1
  combine = pd.DataFrame(
      {
          'letters':letters,
          'appear':appear
          }
      )
  combine = combine.sort_values('appear', ascending = False)

  appear_to_drop = combine['appear'].values.tolist()
  letters_to_drop = combine['letters'].values.tolist()
  number = []
  hold_values = []
  left = []
  right = []
  combo_l = ''
  combo_a = 0
  y = len(letters_to_drop); z = 0
  num = int(len(breakdown))  

  while len(letters_to_drop) != 3:
      number.append(appear_to_drop[-1] + appear_to_drop[-2])
      left.append(letters_to_drop[-1])
      right.append(letters_to_drop[-2])
      combo_l = letters_to_drop[-1] + letters_to_drop[-2]
      combo_a = number[-1]
      letters_to_drop.remove(letters_to_drop[-1])
      letters_to_drop.remove(letters_to_drop[-1])
      letters_to_drop.append(combo_l)
      appear_to_drop.remove(appear_to_drop[-1])
      appear_to_drop.remove(appear_to_drop[-1])
      appear_to_drop.append(combo_a)
      combine_b = pd.DataFrame(
          {
              'letters':letters_to_drop,
              'appear':appear_to_drop
              }
          )
      combine_b = combine_b.sort_values('appear', ascending = False)
      appear_to_drop = combine_b['appear'].values.tolist()
      letters_to_drop = combine_b['letters'].values.tolist()
      y = len(letters_to_drop)

      z = z+1



  left.append(letters_to_drop[-1])
  right.append(letters_to_drop[-2])
  letters_to_drop.remove(letters_to_drop[-1])
  letters_to_drop.remove(letters_to_drop[-1])
  appear_to_drop.remove(appear_to_drop[-1])
  appear_to_drop.remove(appear_to_drop[-1])

  if len(letters_to_drop) == 1:
      left.append(letters_to_drop[-1])
      right.append(left[-2] + right[-1])
      letters_to_drop.remove(letters_to_drop[-1])
      appear_to_drop.remove(appear_to_drop[-1])
  else:
      pass

  left_flip = pd.DataFrame(left)
  left_flip = left_flip.reset_index()
  left_flip = left_flip.sort_values('index',ascending = False)
  left_flip.columns = ['index','left']
  left = left_flip['left'].values.tolist()
  right_flip = pd.DataFrame(right)
  right_flip = right_flip.reset_index()
  right_flip = right_flip.sort_values('index',ascending = False)
  right_flip.columns = ['index','right']
  right = right_flip['right'].values.tolist()

  encoder_index = pd.DataFrame(
      {
        'left': left,
        'right': right
      }
  )
  encoder_index = encoder_index.reset_index()
  encoder_index = encoder_index.sort_values('index',ascending = True)
  encoder_index = encoder_index.set_index('index')
  encoder_index = encoder_index.reset_index(drop = True)
  find = 0
  list_of_codes = []
  while find != len(breakdown):
    find_letter = breakdown[find]
    letter_code_list = []
    b = 0
    while b != len(left):
      if find_letter in list(left[b]):
          letter_code_list.append('0')
          if len(list(left[b])) == 1:
            b = len(left)-1
            list_of_codes.append(letter_code_list)
          else:
            pass
      elif find_letter in list(right[b]):
          letter_code_list.append('1')
          if len(list(right[b])) == 1:
            b = len(right)-1
            list_of_codes.append(letter_code_list)
          else:
            pass
      else:
          pass
      b = b+1
    find = find + 1

  encode_flat = []
  for sublist in list_of_codes:
      for item in sublist:
          encode_flat.append(item)

  encoded = ''
  encoded = encoded.join(encode_flat)
  return encoded

def huffman_random_index(string,index_limit):
  encrypt = list(str(string)) 
  import random
  random_index = str(random.randint(0,index_limit-1))
  random = True
  index = pd.read_csv('https://raw.githubusercontent.com/Zachjaryw/Huffman/main/' + random_index + '.csv')
  left = index['left'].values.tolist()
  right = index['right'].values.tolist()
  find = 0
  list_of_codes = []
  while find != len(encrypt):
    find_letter = encrypt[find]
    letter_code_list = []
    b = 0
    while b != len(left):
      if find_letter in list(left[b]):
          letter_code_list.append('0')
          if len(list(left[b])) == 1:
            b = len(left)-1
            list_of_codes.append(letter_code_list)
          else:
            pass
      elif find_letter in list(right[b]):
          letter_code_list.append('1')
          if len(list(right[b])) == 1:
            b = len(right)-1
            list_of_codes.append(letter_code_list)
          else:
            pass
      else:
          pass
      b = b+1
    find = find + 1
  encoder_index = index
  encode_flat = []
  for sublist in list_of_codes:
      for item in sublist:
          encode_flat.append(item)

  encoded = ''
  encoded = encoded.join(encode_flat)
  encoded = str(encoded) + ':#' + str(random_index)
  return encoded
def huffman_decrypt(string):
  values_list = list(str(string))
  break_pos = values_list.index(':')
  a = values_list[break_pos+2:]
  idx = ''.join(str(elem) for elem in a)
  pull_index = 'https://raw.githubusercontent.com/Zachjaryw/Huffman/main/' + str(idx) + '.csv'
  values_list = values_list[:break_pos]
  
  index = pd.read_csv(pull_index)
  left = index['left'].values.tolist()
  right = index['right'].values.tolist()

  x = 0; combine = []
  while x != len(left):
      combine.append(str(left[x]) + str(right[x]))
      x +=1
  
  result = []
  pos_values = 0
  current = combine[0]

  while len(values_list) - pos_values != 0:
      if values_list[pos_values] == '0':
          check = len(current)
          if check == 1:
              result.append(current)
              current = combine[0]
          else:
              combine_pos = combine.index(current)
              current = left[combine_pos]
              pos_values += 1
      elif values_list[pos_values] == '1':
          check = len(current)
          if check == 1:
              result.append(current)
              current = combine[0]
          else:
              combine_pos = combine.index(current)
              current = right[combine_pos]
              pos_values += 1
      else:
          print('error')
          pos_values = len(values_list)

  if current != combine[0]:
      result.append(current)
  else:
      pass
  encoder_index = index
  final = ''
  result = final.join(result)
  return result

def huffman_encrypt_list_random(list_name,index_limit):
  position_in_list = 0
  new_list = []
  while position_in_list != len(list_name):
    new_list.append(huffman_random_index(list_name[position_in_list],index_limit))
    position_in_list += 1

  return new_list

def huffman_decrypt_list_random(list_name):
  position_in_list = 0
  new_list = []
  while position_in_list != len(list_name):
    new_list.append(huffman_decrypt(list_name[position_in_list]))
    position_in_list += 1
  return new_list
def list_to_df(list_name):
  to_df = pd.DataFrame({
      'Column': list_name
  }
  )
  return to_df

def huffman_encrypt_df_csv(file_name,index_limit):
  df_name = pd.read_csv(file_name)
  df_name = df_name.replace(r'', 'NaN')
  current_column = 0
  new_df = pd.DataFrame({})
  while current_column != len(df_name.columns):
    new_list = df_name[df_name.columns[current_column]].values.tolist()
    encrypted_list = huffman_encrypt_list_random(new_list,index_limit)
    new_df = pd.concat([new_df,list_to_df(encrypted_list)],axis = 1)
    current_column += 1
  new_df.columns = df_name.columns
  return new_df

def huffman_decrypt_df_csv(file_name,index_column = 0):
  df_name = pd.read_csv(file_name,index_col=index_column)
  current_column = 0
  new_df = pd.DataFrame({})
  while current_column != len(df_name.columns):
    new_list = df_name[df_name.columns[current_column]].values.tolist()
    encrypted_list = huffman_decrypt_list_random(new_list)
    new_df = pd.concat([new_df,list_to_df(encrypted_list)],axis = 1)
    current_column += 1
  new_df.columns = df_name.columns
  return new_df
def save_file_csv(file_name,data):
    if file_name == "/Users/USERNAME/Downloads/FILENAME.csv":
        pass
    else:
        data.to_csv(file_name)

st.title("Huffman Encryption")
st.header("Encrypt (random index)","Hello World")
string1 = st.text_input("Encrypt:")
st.write(huffman_random_index(string1,1000))

st.header("Encrypt (self index)")
string2 = st.text_input("Encrypt (must contain more than 3 unique characters):","Hello World")
st.write(huffman_encrypt(string2))
st.write(huffman_index(string2))

st.header("Decrypt (must have :#___)")
string3 = st.text_input("Decrypt:","01111001010110111101111110110110100001001011111011010001101011111011101110:#870")
st.write(huffman_decrypt(string3))

st.header("Encrypt dataframe from CSV file")
file1 = st.file_uploader("Upload File (It may take some time to complete depending on file size)",type="csv")
if file1 is not None:
  encrypted = huffman_encrypt_df_csv(file1,1000)
  st.write(encrypted)
  save_file = st.text_input("To Save File, adjust entry below to save to downloads file on Mac computer","/Users/USERNAME/Downloads/FILENAME.csv")
  save_file_csv(save_file,encrypted)

st.header("Decrypt dataframe from CSV file")
file2 = st.file_uploader("Upload Encrypted File (It may take some time to complete depending on file size)",type="csv")
if file2 is not None:
  decrypted = huffman_decrypt_df_csv(file2)
  st.write(decrypted)
  save_file1 = st.text_input("To Save Unencrypted File, adjust entry below to save to downloads file on Mac computer","/Users/USERNAME/Downloads/FILENAME.csv")
  save_file_csv(save_file1,decrypted)

