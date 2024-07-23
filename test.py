import sympy as sp

# 定义变量
I, bits = sp.symbols('I bits')

# 定义公式
m_formula = 4.4e-6 * I**2 + 3.8e-5 * I + 0.00178
I_formula = 0.000152668 * bits + 0.0026

# 代入
m_formula_substituted = m_formula.subs(I, I_formula)

# 化简结果
m_formula_simplified = sp.simplify(m_formula_substituted)

print(m_formula_simplified)
