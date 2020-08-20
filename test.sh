# pytest test/

echo "running pylint..."

pylint  --max-line-length=120 --disable=R0801 src/

echo "running mypy..."

mypy --ignore-missing-imports src/

echo "running flake8..."

flake8  --max-line-length 120 src/ test/
