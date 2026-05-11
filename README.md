# CSVReporter

Утилита для чтения CSV-файлов со статистикой видео и построения отчётов.

## Установка

```bash
uv pip install -e .
```

## Использование

```bash
python main.py --files stats1.csv stats2.csv --report clickbait
```

### Параметры

| Аргумент | Описание |
|----------|----------|
| `--files` | Список CSV-файлов для обработки |
| `--report` | Тип отчёта (см. `app/report_builders.py`) |

### Доступные отчёты

- `clickbait` — видео с высоким CTR (>15%) и низким удержанием (<40%), отсортированные по CTR

## Тестирование

```bash
uv run pytest
```

## Расширение

1. Создайте класс отчёта в `app/report_builder.py`, унаследовавшись от `BaseReportBuilder`
2. Задайте `filtering_parameter` и/или `sorting_parameter` и `descending_order`
3. Зарегистрируйте в `app/report_builders.py`
