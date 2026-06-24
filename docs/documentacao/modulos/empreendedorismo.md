---
layout: default
title: "Módulo de Empreendedorismo"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas](/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »](/documentacao/caminho_do_arquivo) 
-->

[Anterior: Módulo de Salários](/documentacao/modulos/salarios)

# {{ page.title }}

> **Vinculação societária formal dos egressos.** Mensura a vinculação formal de egressos da RFEPCT à criação de empresas e à participação societária registrada em bases administrativas, oferecendo leitura complementar à inserção ocupacional.

## Escopo e leitura

O módulo mensura a vinculação formal de egressos da RFEPCT à criação de empresas e à participação societária registrada em bases administrativas. Utiliza os egressos como população de referência e os registros societários como evidência operacional de atividade empreendedora.

O indicador não equivale à ocupação formal e não substitui os indicadores dos módulos de Empregabilidade e Salários. Um egresso pode empreender sem constar como empregado na RAIS, acumular vínculo empregatício e participação empresarial ou ainda estar vinculado a mais de uma empresa.

O módulo permite analisar essa inserção por curso, perfil do egresso, território e características das empresas, e oferece leitura complementar da trajetória pós-formação.

### Estrutura do módulo

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 30%"><strong>Indicadores centrais</strong></td><td>Total de empreendedores · Total de egressos · Taxa de empreendedorismo · Empresas criadas · Capital social médio.</td></tr>
    <tr><td><strong>Indicadores desagregados</strong></td><td>Empreendedorismo por UF · campus · curso · tipo de curso · turno · sexo · faixa etária · cor ou raça · ano de conclusão · região · atividade econômica · situação cadastral · porte.</td></tr>
  </tbody>
</table>

> **Acumulação de inserções.** Um mesmo egresso pode ser simultaneamente ocupado (Módulo 01) e empreendedor (Módulo 03). Os indicadores destes módulos devem ser lidos como dimensões complementares, não excludentes, da trajetória pós-formação.

## Indicadores centrais

### 01 · Total de empreendedores · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Indica o total de egressos identificados em quadros societários de empresas.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Valores mais elevados sugerem maior presença de egressos em atividade empreendedora. A leitura deve considerar, simultaneamente, o total de egressos da base analisada.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Total de empreendedores = ∑ (empreendedores)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>CNPJ · PNP 2017–2022</td></tr>
  </tbody>
</table>

### 02 · Total de egressos · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Mensura o total de egressos da RFEPCT no período de referência. Quando houver múltiplas formações associadas ao mesmo egresso, deve-se priorizar a formação de maior nível, evitando duplicidades.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Valores mais elevados indicam maior cobertura da RFEPCT e maior alcance institucional. Sua interpretação não deve ser associada, isoladamente, à qualidade dos resultados obtidos.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Total de egressos = ∑ (egressos)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>CNPJ · PNP 2017–2022</td></tr>
  </tbody>
</table>

### 03 · Taxa de empreendedorismo · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Mensura a proporção de egressos identificados como empreendedores, considerando os filtros aplicados. É o indicador central do módulo: permite avaliar a incidência relativa de atividade empreendedora entre os egressos.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, maior a incidência relativa de empreendedorismo entre os egressos do recorte analisado. A interpretação deve considerar o total de egressos, para evitar leituras distorcidas em recortes com baixo volume absoluto.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Taxa de empreendedorismo (%) = ( Empreendedores / Egressos ) × 100</td></tr>
    <tr><td><strong>Fontes</strong></td><td>CNPJ · PNP 2017–2022</td></tr>
  </tbody>
</table>

### 04 · Empresas criadas · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Contabiliza o número de empresas com participação societária de egressos da RFEPCT, incluindo matrizes e filiais, conforme os filtros aplicados.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, maior o volume empresarial formal identificado entre os egressos.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Empresas criadas = Total de matrizes + Total de filiais</td></tr>
    <tr><td><strong>Fontes</strong></td><td>CNPJ · PNP 2017–2022</td></tr>
  </tbody>
</table>

### 05 · Capital social médio · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Contabiliza o capital social declarado pelas empresas associadas aos egressos da RFEPCT, somando matrizes e filiais, conforme os filtros aplicados.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, maior o volume de capital social declarado pelas empresas associadas aos egressos.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Capital social = ∑ capital social declarado das empresas associadas aos egressos</td></tr>
    <tr><td><strong>Fontes</strong></td><td>CNPJ · PNP 2017–2022</td></tr>
  </tbody>
</table>

> **Notas de leitura.** O capital social declarado é uma medida cadastral, não necessariamente reflete o capital investido ou em circulação. Recomenda-se a leitura conjunta com o número de empresas criadas e a taxa de empreendedorismo para caracterizar o porte e a densidade do empreendedorismo no recorte analisado.

## Indicadores desagregados

Detalham a composição interna dos resultados identificados pelos indicadores centrais. Caracterizam como os empreendimentos se distribuem segundo sexo, faixa etária, curso, setor econômico, porte empresarial, natureza jurídica, território ou características institucionais.

> **Universo de referência.** As análises consideram exclusivamente os egressos identificados como sócios ou responsáveis por empresas formalmente registradas nas bases administrativas utilizadas.

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th style="width: 30%; text-align: center">Indicador</th>
      <th style="width: 40%; text-align: center">Descrição</th>
      <th style="width: 30%; text-align: center">Finalidade</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Taxa de empreendedorismo por UF</td><td>Percentual de egressos identificados como empreendedores formais em cada UF.</td><td>Identificar diferenças territoriais na atividade empreendedora.</td></tr>
    <tr><td>Total de empreendedores por campus</td><td>Quantidade de egressos identificados como sócios ou responsáveis por empresas em cada campus.</td><td>Comparar a participação empreendedora entre unidades institucionais.</td></tr>
    <tr><td>Taxa de empreendedorismo por curso</td><td>Percentual de empreendedores segundo o curso concluído.</td><td>Analisar diferenças associadas às formações ofertadas.</td></tr>
    <tr><td>Taxa de empreendedorismo por tipo de curso</td><td>Percentual de empreendedores segundo a tipologia da formação cursada.</td><td>Comparar padrões de empreendedorismo entre modalidades formativas.</td></tr>
    <tr><td>Taxa de empreendedorismo por turno</td><td>Percentual de empreendedores segundo o turno de oferta do curso.</td><td>Identificar diferenças relacionadas à organização temporal da formação.</td></tr>
    <tr><td>Taxa de empreendedorismo por sexo</td><td>Percentual de empreendedores segundo sexo.</td><td>Identificar desigualdades de participação entre homens e mulheres.</td></tr>
    <tr><td>Taxa de empreendedorismo por faixa etária</td><td>Percentual de empreendedores segundo grupos etários.</td><td>Analisar diferenças ao longo do ciclo de vida laboral.</td></tr>
    <tr><td>Taxa de empreendedorismo por cor ou raça</td><td>Percentual de empreendedores segundo categorias de cor ou raça.</td><td>Identificar desigualdades de participação entre grupos raciais.</td></tr>
    <tr><td>Taxa de empreendedorismo por ano de conclusão</td><td>Percentual de empreendedores segundo o ano de conclusão do curso.</td><td>Acompanhar diferenças temporais entre coortes de egressos.</td></tr>
    <tr><td>Empresa e capital médio por UF</td><td>Quantidade média de empresas e valor médio de capital social das empresas vinculadas aos egressos em cada UF.</td><td>Analisar a distribuição territorial da estrutura econômica dos empreendimentos.</td></tr>
    <tr><td>Taxa de empreendedorismo por região</td><td>Percentual de empreendedores segundo grandes regiões geográficas.</td><td>Identificar diferenças regionais na atividade empreendedora.</td></tr>
    <tr><td>Empresas por atividade econômica</td><td>Distribuição das empresas vinculadas aos egressos segundo setores de atividade definidos pela CNAE.</td><td>Identificar os segmentos econômicos que concentram os empreendimentos.</td></tr>
    <tr><td>Taxa de empreendedorismo por situação cadastral</td><td>Distribuição dos empreendedores segundo a situação cadastral das empresas registradas.</td><td>Avaliar padrões de permanência, encerramento ou regularidade dos empreendimentos.</td></tr>
    <tr><td>Empresas por porte</td><td>Distribuição das empresas vinculadas aos egressos segundo o porte empresarial.</td><td>Caracterizar a estrutura e dimensão econômica dos empreendimentos.</td></tr>
  </tbody>
</table>

**Fontes consolidadas do módulo:** IBGE — CNAE 2.3 · IBGE — DTB 2024 · CNPJ · PNP 2017–2022

[Anterior: Módulo de Salários](/documentacao/modulos/salarios)
[Próximo: Módulo de Trajetória Acadêmica »](/documentacao/modulos/trajetoria_academica)
