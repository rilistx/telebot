# -> pip install aiocryptopay
#
#
#
# from aiocryptopay import AioCryptoPay, Networks
# import asyncio
#
# crypto = AioCryptoPay(token='153130:AAvjpMtBVL2XQB22InumnW7OVjit6994wq8', network=Networks.MAIN_NET)
#
#
# async def main() -> None:
#     profile = await crypto.get_me()
#     currencies = await crypto.get_currencies()
#     balance = await crypto.get_balance()
#     rates = await crypto.get_exchange_rates()
#
#     print(profile, currencies, balance, rates, sep='\n')
#     print(balance)
#
#     invoice = await crypto.create_invoice(asset='USDT', amount=1.0)
#     print(invoice.bot_invoice_url)
#
#     id_invoice = invoice.invoice_id
#     print(id_invoice)
#
#     while True:
#         a = input("напиши что то.... : ")
#
#         old_invoice = await crypto.get_invoices(invoice_ids=id_invoice)
#         print(old_invoice.status)
#
#         if a == '0':
#             break
#
#     deleted_invoice = await crypto.delete_invoice(invoice_id=id_invoice)
#     print(deleted_invoice)
#
#     while True:
#         print(input("напиши что то.... : "))
#
#         old_invoice = await crypto.get_invoices(invoice_ids=id_invoice)
#         print(old_invoice.status)
#
#     await crypto.transfer(
#         user_id=406105379, asset='USDT', amount=1, spend_id='QWERTY9939126', comment='Вывод с Betting Bot'
#     )
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
