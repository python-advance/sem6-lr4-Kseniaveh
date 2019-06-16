import random
class TruthTable(object):
  def __init__(self):
        """Constructor"""
        self.p_or = TruthItem([[0,0], [1,0], [0,1], [1,1]],[0, 1, 1, 1])
        self.p_and = TruthItem([[0,0], [1,0], [0,1], [1,1]],[0, 0, 0, 1])
        self.p_not = TruthItem([0, 1],[1, 0])
        self.p_xor=TruthItem([[0,0], [1,0], [0,1], [1,1]],[0, 1, 1, 0])
        self.p_xnor=TruthItem([[0,0], [1,0], [0,1], [1,1]],[1, 0, 0, 1])

class TruthItem(object):
  def __init__(self,_data,_data_result):
        """Constructor"""
        self.data = _data
        self.data_result = _data_result

class Perceptron(object):
  def __init__(self,_theta1,_theta2,_theta3):
        """Constructor"""
        self.theta1 = _theta1
        self.theta2 = _theta2
        self.theta3 = _theta3
        self.truthtable=TruthTable()
        
  def sigmoid(self,x):
    import math    
    return 1.0 / (1 + math.exp(-x))
  
  def func1(self,x):
      result = self.sigmoid(self.theta1 + x * self.theta2)
      if(result >= 0.5):
        return 1
      else:
        return 0

  def func2(self,x, y):
	  result = self.sigmoid(self.theta1 + x * self.theta2 + y * self.theta3)
	  if(result >= 0.5):
		  return 1
	  else:
		  return 0
  

  def check_thetas_or(self):
    for i in range(len(self.truthtable.p_or.data)):
      result = self.func2(self.truthtable.p_or.data[i][0], self.truthtable.p_or.data[i][1])
      if(self.truthtable.p_or.data_result[i] != result):
        return False
    return True

  def check_thetas_and(self):    
    for i in range(len(self.truthtable.p_and.data)):
      result = self.func2(self.truthtable.p_and.data[i][0], self.truthtable.p_and.data[i][1])
      if(self.truthtable.p_and.data_result[i] != result):
        return False
    return True

  def check_thetas_not(self):   
    for i in range(len(self.truthtable.p_not.data)):
      result = self.func1(self.truthtable.p_not.data[i])
      if(self.truthtable.p_not.data_result[i] != result):
        return False
    return True

  def printTruthTable(self,table):
    for i in range(len(table.data)):
      print(table.data[i][0], '|', table.data[i][1], '|', table.data_result[i])

  def printTruthTableNOT(self,table):
    for i in range(len(table.data)):
      print(table.data[i], '|', table.data_result[i])    

    
	  
print('-----------------------OR - HardCode:-----------------------')
PerOr=Perceptron(5,5,5)
print('Thetas 5,5,5 is '+str(PerOr.check_thetas_or()))

PerOr=Perceptron(-10,20,20)
print('Thetas -10,20,20 is '+str(PerOr.check_thetas_or()))        


print('-----------------------OR - Random:-----------------------')
while(True):
  PerOr=Perceptron(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20))
  result=PerOr.check_thetas_or()
  if(result):
    print('Find thetas OR!!!')
    print('Thetas '+str(PerOr.theta1)+','+str(PerOr.theta2)+','+str(PerOr.theta3)+' is '+str(PerOr.check_thetas_or()))
    PerOr.printTruthTable(PerOr.truthtable.p_or)   
    break

print('-----------------------AND - Random:-----------------------')
while(True):
  PerAnd=Perceptron(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20))
  result=PerAnd.check_thetas_and()
  if(result):
    print('Find thetas AND!!!')
    print('Thetas '+str(PerAnd.theta1)+','+str(PerAnd.theta2)+','+str(PerAnd.theta3)+' is '+str(PerAnd.check_thetas_and()))
    PerAnd.printTruthTable(PerAnd.truthtable.p_and)       
    break

print('-----------------------NOT - Random:-----------------------')
while(True):
  PerNot=Perceptron(random.randint(-20, 20), random.randint(-20, 20), random.randint(-20, 20))
  result=PerNot.check_thetas_not()
  if(result):
    print('Find thetas NOT!!!')
    print('Thetas '+str(PerNot.theta1)+','+str(PerNot.theta2)+' is '+str(PerNot.check_thetas_not()))
    PerNot.printTruthTableNOT(PerNot.truthtable.p_not)    
    break
				
print('-----------------------XOR:-----------------------')
trTable=TruthTable()
for i in range(len(trTable.p_xor.data)):
	x = trTable.p_xor.data[i][0]
	y = trTable.p_xor.data[i][1]
	not_x = PerNot.func1(x)
	not_y = PerNot.func1(y)
	left = PerAnd.func2(not_x, y)
	right = PerAnd.func2(x, not_y)
	result = PerOr.func2(left, right)	
	print(x, '|', y, '|', result)
	assert(trTable.p_xor.data_result[i] == result)

print('-----------------------XNOR:-----------------------')
for i in range(len(trTable.p_xnor.data)):
	x = trTable.p_xnor.data[i][0]
	y = trTable.p_xnor.data[i][1]
	not_x = PerNot.func1(x)
	not_y = PerNot.func1(y)
	left = PerAnd.func2(not_x, y)
	right = PerAnd.func2(x, not_y)
	result = PerOr.func2(left, right)	
	result = PerNot.func1(result)	
	print(x, '|', y, '|', result)
	assert(trTable.p_xnor.data_result[i] == result)		
