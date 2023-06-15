
def cycle_sort(arr):
    n = len(arr)
    
    for ciclo_inicio in range(n-1):
        item_atual = arr[ciclo_inicio]
        posicao_correta = ciclo_inicio
        
        for i in range(ciclo_inicio+1, n):
            if arr[i] < item_atual:
                posicao_correta += 1
        
        if posicao_correta == ciclo_inicio:
            continue
        
        while item_atual == arr[posicao_correta]:
            posicao_correta += 1
        
        arr[posicao_correta], item_atual = item_atual, arr[posicao_correta]
        
        while posicao_correta != ciclo_inicio:
            posicao_correta = ciclo_inicio
            
            for i in range(ciclo_inicio+1, n):
                if arr[i] < item_atual:
                    posicao_correta += 1
            
            while item_atual == arr[posicao_correta]:
                posicao_correta += 1
            
            arr[posicao_correta], item_atual = item_atual, arr[posicao_correta]
    
    return arr
    
array = [9, 60, 20, 2, 10, 12, 1]
    
cycle_sort(array)
    
print(array)