---
layout: default
title: "Módulo de Salários"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas](/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »](/documentacao/caminho_do_arquivo) 
-->

[Anterior: Módulo de Empregabilidade](/documentacao/modulos/empregabilidade)

# {{ page.title }}

> **Remuneração no mercado formal de trabalho.** Mensura a remuneração dos egressos inseridos no mercado de trabalho formal por meio das informações salariais registradas em vínculos empregatícios identificados nas bases administrativas, considerando rendimento, dispersão e perfis comparativos.

## Escopo e leitura

O módulo de Salários mensura a remuneração dos egressos inseridos no mercado de trabalho formal por meio das informações salariais registradas em vínculos empregatícios identificados nas bases administrativas. Os indicadores utilizam exclusivamente os egressos com vínculo formal ativo como população de referência.

O módulo contempla indicadores relacionados à remuneração média, à distribuição salarial e à evolução dos rendimentos dos egressos ocupados, de acordo com o ano-base da RAIS. As análises podem ser realizadas em diferentes horizontes temporais e níveis de agregação institucional, territorial, ocupacional e sociodemográfica.

Os indicadores não capturam rendimentos provenientes de atividades não registradas formalmente, incluindo trabalho informal, trabalho autônomo sem vínculo administrativo, empreendedorismo sem constituição formal, atividades eventuais ou outras formas de geração de renda não identificáveis nas bases utilizadas. Portanto, os resultados devem ser interpretados como medidas de remuneração no mercado formal de trabalho, restritas aos egressos com vínculo empregatício identificado.

A comparação dos indicadores salariais exige atenção às diferenças na composição dos grupos analisados, especialmente quanto ao número de egressos ocupados, perfil ocupacional, setor econômico, unidade federativa e características sociodemográficas dos indivíduos.

### Estrutura do módulo

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 30%"><strong>Indicadores centrais</strong></td><td>Massa salarial · Salário médio ponderado · Mediana salarial ponderada · Média logarítmica ponderada · Desvio padrão salarial · Salário médio relativo.</td></tr>
    <tr><td><strong>Indicadores desagregados</strong></td><td>Salário médio por UF · curso · tipo de curso · turno · sexo · faixa etária · cor ou raça · natureza do vínculo · ano de conclusão · setor econômico · mesorregiões.</td></tr>
  </tbody>
</table>

> **Limites de comparabilidade.** Comparações entre grupos exigem atenção ao tamanho do grupo, ao perfil ocupacional e ao setor econômico. Recomenda-se a leitura conjunta de média, mediana e dispersão para evitar interpretações distorcidas em distribuições assimétricas.

## Indicadores centrais

### 01 · Massa salarial · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Soma dos salários brutos dos egressos ocupados no recorte selecionado.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor apenas como volume agregado. Não deve ser usada isoladamente para comparar grupos de tamanhos diferentes.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Massa salarial = ∑ S<sub>i</sub><br><em>S<sub>i</sub></em>: salário bruto do egresso i com vínculo formal de trabalho na RAIS de referência.</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · RAIS 2023</td></tr>
  </tbody>
</table>

### 02 · Salário médio ponderado · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Mede a remuneração média dos egressos ocupados, ponderando cada grupo pelo número de ocupados.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor — desde que analisado junto à mediana, à dispersão e ao tamanho do grupo.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Salário médio ponderado = ∑ ( S̄<sub>g</sub> × N<sub>g</sub> ) / ∑ N<sub>g</sub><br><em>S̄<sub>g</sub></em>: salário médio dos egressos ocupados no grupo g.<br><em>N<sub>g</sub></em>: número de egressos ocupados no grupo g (peso de S̄<sub>g</sub>).<br><em>∑ N<sub>g</sub></em>: quantidade total de egressos com vínculo formal na RAIS de referência.</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · RAIS 2023</td></tr>
  </tbody>
</table>

### 03 · Mediana salarial ponderada · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Representa o ponto central da distribuição salarial dos egressos ocupados.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor. Em distribuições assimétricas, tende a ser mais estável que a média.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Mediana salarial ponderada = mediana( Salário , peso = N<sub>ocupados</sub> )</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · RAIS 2023</td></tr>
  </tbody>
</table>

### 04 · Média logarítmica ponderada · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Mede a remuneração média com transformação logarítmica, reduzindo a influência de valores extremos sobre o resultado.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor. Deve ser interpretada como medida comparativa — e não como valor nominal direto — quando exibida em escala logarítmica.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Média log. ponderada = ∑ ( log(Salário) × N<sub>ocupados</sub> ) / ∑ N<sub>ocupados</sub></td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · RAIS 2023</td></tr>
  </tbody>
</table>

### 05 · Desvio padrão salarial · *Quanto menor, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Mede a dispersão dos salários em torno da média salarial do grupo.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto menor, melhor quando o objetivo é menor desigualdade interna. Não indica, sozinho, melhor remuneração.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Desvio padrão = √ [ ∑ ( S<sub>i</sub> − S̄ )² / n ]<br><em>S<sub>i</sub></em>: salário individual do egresso i. <em>S̄</em>: média salarial do grupo. <em>n</em>: número de egressos ocupados no grupo.</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · RAIS 2023</td></tr>
  </tbody>
</table>

### 06 · Salário médio relativo · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Compara o salário médio dos egressos com uma referência salarial externa ou geral.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor. Valores acima de 1 indicam salário superior à referência.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Salário relativo = Salário médio dos egressos / Salário médio de referência</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · RAIS 2023</td></tr>
  </tbody>
</table>

## Indicadores desagregados

Os indicadores desagregados detalham a composição interna dos resultados salariais. Caracterizam como os rendimentos se distribuem segundo sexo, faixa etária, curso, setor econômico, natureza do vínculo, território, ocupação ou características institucionais.

> **Universo de referência.** No módulo de Salários, as análises consideram exclusivamente os egressos identificados com vínculo formal de trabalho e com informação salarial disponível nas bases administrativas utilizadas.

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th style="width: 30%; text-align: center">Indicador</th>
      <th style="width: 40%; text-align: center">Descrição</th>
      <th style="width: 30%; text-align: center">Finalidade</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Salário médio por UF</td><td>Média da remuneração dos ocupados segundo a UF do vínculo formal.</td><td>Identificar diferenças territoriais de rendimento entre os egressos.</td></tr>
    <tr><td>Massa salarial por UF</td><td>Soma dos rendimentos dos ocupados em cada UF.</td><td>Identificar a concentração territorial da renda do trabalho dos egressos.</td></tr>
    <tr><td>Salário médio por curso</td><td>Média da remuneração dos ocupados segundo o curso concluído.</td><td>Comparar retornos salariais associados às diferentes formações ofertadas.</td></tr>
    <tr><td>Salário médio por tipo de curso</td><td>Média da remuneração dos ocupados segundo a tipologia da formação.</td><td>Comparar padrões salariais entre modalidades formativas distintas.</td></tr>
    <tr><td>Salário médio por turno</td><td>Média da remuneração dos ocupados segundo o turno de oferta do curso.</td><td>Identificar diferenças salariais associadas à organização temporal da formação.</td></tr>
    <tr><td>Salário médio por sexo</td><td>Média da remuneração dos ocupados segundo sexo.</td><td>Identificar desigualdades salariais entre homens e mulheres.</td></tr>
    <tr><td>Salário médio por faixa etária</td><td>Média da remuneração dos ocupados segundo grupos etários.</td><td>Analisar diferenças de rendimento ao longo do ciclo de vida laboral.</td></tr>
    <tr><td>Salário médio por cor ou raça</td><td>Média da remuneração dos ocupados segundo categorias de cor ou raça.</td><td>Identificar desigualdades salariais associadas a grupos raciais.</td></tr>
    <tr><td>Salário médio por natureza do vínculo</td><td>Média da remuneração segundo a natureza jurídica ou administrativa do vínculo empregatício.</td><td>Comparar padrões salariais entre diferentes tipos de vínculo.</td></tr>
    <tr><td>Salário médio por ano de conclusão</td><td>Média da remuneração dos ocupados segundo o ano de conclusão do curso.</td><td>Analisar diferenças temporais de rendimento entre coortes de egressos.</td></tr>
    <tr><td>Salário relativo por sexo</td><td>Relação entre o salário médio de grupos de sexo distintos em relação a um grupo de referência.</td><td>Mensurar desigualdades salariais relativas entre homens e mulheres.</td></tr>
    <tr><td>Salário relativo por tipo de curso</td><td>Relação entre os salários médios de diferentes tipos de curso em relação a uma categoria de referência.</td><td>Comparar retornos salariais relativos entre modalidades formativas.</td></tr>
    <tr><td>Salário relativo por mesorregiões</td><td>Relação entre os salários médios das diferentes mesorregiões em relação a uma mesorregião de referência.</td><td>Identificar desigualdades regionais relativas nos rendimentos dos egressos.</td></tr>
    <tr><td>Salário relativo por setor econômico</td><td>Relação entre os salários médios dos setores econômicos em relação a um setor de referência.</td><td>Comparar diferenças relativas de remuneração entre segmentos econômicos.</td></tr>
  </tbody>
</table>

**Fontes consolidadas do módulo:** IBGE — CBO‑2002 v. 2026 · IBGE — DTB 2024 · IBGE — CNAE 2.3 · PNP 2017–2022 · RAIS 2023

> **Recomendações de leitura.** 1. Apresentar média, mediana e dispersão lado a lado em distribuições assimétricas. 2. Em recortes com poucos ocupados, priorizar a mediana e indicar a contagem do grupo. 3. Em análises temporais, indicar o ano-base utilizado para conversão de valores e o índice deflator quando aplicável.

[Anterior: Módulo de Empregabilidade](/documentacao/modulos/empregabilidade)
[Próximo: Módulo de Empreendedorismo »](/documentacao/modulos/empreendedorismo)
