status = input("Введите статус заказа (pending/processing/shipped/delivered/cancelled): ")

match status:
    case "pending":
        status = "В ожидании"
        description = "Заказ принят и ожидает подтверждения"
        emoji = "⏳"
        time_estimate = "1-24 часа"
    case "processing":
        status = "В обработке"
        description = "Заказ подтвержден и готовится к отправке"
        emoji = "📦"
        time_estimate = "1-3 дня"
    case "shipped":
        status = "Отправлено"
        description = "Заказ передан в службу доставки"
        emoji = "🛫"
        time_estimate = "1-7 дней"
    case "delivered":
        status = "Доставлено"
        description = "Заказ успешно доставлен получателю"
        emoji = "📨"
        time_estimate = "Завершено"
    case "cancelled":
        status = "Отменено"
        description = "Заказ был отменен"
        emoji = "❌"
        time_estimate = "Не известно"
    case _:
        status = "Неизвестный статус"
        description = "Проверьте правильность введенного статуса"
        emoji = "❓"
        time_estimate = "----"

print("="*30)
print("📦ИНФОРМАЦИЯ О ЗАКАЗЕ📦")
print("="*30)
print(f"Статус: {status}", emoji)
print(f"Этап заказа: {description}")
print(f"Примерное время ожидания: {time_estimate}")
print("="*30)