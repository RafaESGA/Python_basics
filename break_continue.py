def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    
    texto = input('Escribe un texto: ')
    for i in texto:
        if i == 'o':
            break
        print(i)


if __name__ == '__main__':
    run()