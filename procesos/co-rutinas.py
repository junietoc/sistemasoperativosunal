# ejercicio de co rutinas: se corren concurrentemente, usando la funcion gather(), dos funciones:
# even() imprime los numeros pares de 0 a 10
# odd() imprime los numeros impares de 0 a 10
import asyncio
async def main ():
    await asyncio.gather(even(),odd())

async def even():
    even = [x for x in range(11) if x%2 == 0]
    for x in even:
        print(x)
        await asyncio.sleep(1)


async def odd():
    odd = [x for x in range(11) if x%2 == 1]
    for x in odd:
        print(x)
        await asyncio.sleep(1)
asyncio.run(main())