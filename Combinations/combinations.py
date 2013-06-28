    
options = [
    ["blue","green","yellow","brown","red","black","white"], # sizes
    ["1","2","3","4","5","6","7","8"],
    ["one","two","three","four","five","six","seven","eight"],
    ["jorge","george","john","jon","johnny"],
    ["10","9","8","7","6","5","4","3","2","1"],
    ["leather","plastic","wood"],
    ["more otpions","even more options","way too many options"]
]
# Manual Way
count_1 = 0
for option1 in options[0]: 
    for option2 in options[1]: 
        for option3 in options[2]: 
            for option4 in options[3]: 
                for option5 in options[4]:
                    for option6 in options[5]:
                        for option7 in options[6]:
                            print option1, "-", option2, "-",option3,"-",option4,"-",option5,"-",option6, "-",option7
                            count_1 += 1
print count_1
# Programatic Way
def superFunction(options):
    global finalListOfOptions
    finalListOfOptions   = []
    def goThroughEachOne(options, level, listOfoptions):
        global finalListOfOptions
        if(level < len(options)):
            # print "Option Exists - ", level
            for option in options[level]:
                try:
                    listOfoptions[level] = (option)
                except:
                    listOfoptions.append(option)
                goThroughEachOne(options, level + 1, listOfoptions)
        else:
            # This is probably the ugliest part of the whole thing, but, for some reason. .append(listOfoptions) wasn't working for me
            finalListOfOptions.append([])
            finalListOfOptions[len(finalListOfOptions) - 1].extend(listOfoptions)

    goThroughEachOne(options, 0, [])
    return finalListOfOptions
finalListOfOptions = superFunction(options)
# Testing
for combination in finalListOfOptions:
    print combination
print len(finalListOfOptions)
# Comparrison
print "Length on Manual One: ", count_1 , " - superFunction: ", len(finalListOfOptions)
if(count_1 == len(finalListOfOptions)):
    print "Congratulations, Jorge. You figured it out without crying!"
else:
    print "No Match :("