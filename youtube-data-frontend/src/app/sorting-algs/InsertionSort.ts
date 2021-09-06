export class InsertionSort<Type>{

    sort(collection: Type[], property: string, order: string){
        let p = property as keyof Type;
        let i, key, j; 
        for (i = 1; i < collection.length; i++)
        { 
            key = collection[i]; 
            j = i - 1; 
    
            if(order === 'desc'){
              while (j >= 0 && collection[j][p] <= key[p])
              { 
                collection[j + 1] = collection[j]; 
                  j = j - 1; 
              } 
            } else{
              while (j >= 0 && collection[j][p] > key[p])
              { 
                collection[j + 1] = collection[j]; 
                  j = j - 1; 
              } 
            }
            collection[j + 1] = key; 
        } 
      }
      
}

