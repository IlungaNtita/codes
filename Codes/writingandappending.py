#to create a new file and write to it
createfile=open("text.txt","w")
text="This is what i have written"
createfile.write(text)
createfile.close()

#to append to a txt file
appendfile=open("text.txt","a")
text2="\nThis is what i have appended"
appendfile.write(text2)
appendfile.close()
#close file to save it

print(open("text.txt","r").read())