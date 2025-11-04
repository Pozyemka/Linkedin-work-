def factorial(n):

    if not isinstance(n, int) or n < 0:
      
        return None
   
    if n == 0:
        return 1
    
 
    result = 1
    for i in range(n, 0, -1):
        result = result * i
        
    return result