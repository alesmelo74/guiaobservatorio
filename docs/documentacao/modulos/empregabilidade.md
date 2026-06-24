---
layout: default
title: "Módulo de Empregabilidade"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas](/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »](/documentacao/caminho_do_arquivo) 
-->

[Anterior: Visão geral dos módulos](/documentacao/apresentacao/visao_geral_dos_modulos)

# {{ page.title }}

> **Inserção formal no mercado de trabalho.** Mensura a inserção dos egressos no mercado de trabalho formal por meio da identificação de vínculos empregatícios registrados em bases administrativas, com atenção à distribuição territorial e à adequação entre formação e ocupação.

## Escopo e leitura

O módulo mensura a inserção dos egressos no mercado de trabalho formal por meio da identificação de vínculos empregatícios registrados em bases administrativas. Os indicadores utilizam os egressos da RFEPCT como população de referência e os vínculos formais de trabalho como evidência operacional de ocupação.

O módulo contempla indicadores relacionados à inserção ocupacional de acordo com o ano-base da RAIS. As análises podem ser realizadas em diferentes horizontes temporais e níveis de agregação institucional, territorial e sociodemográfica.

Os indicadores não capturam modalidades de inserção não registradas em vínculos formais, incluindo trabalho informal, trabalho autônomo sem registro administrativo, ocupações eventuais e outras formas de geração de renda não identificáveis nas bases utilizadas.

Os resultados devem, portanto, ser interpretados como medidas de inserção formal no mercado de trabalho — e não como medida abrangente de ocupação econômica dos egressos.

### Quadro síntese de resultados (PNP 2017–2022 · RAIS 2023)

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th style="text-align: center">Total de egressos</th>
      <th style="text-align: center">Total de ocupados</th>
      <th style="text-align: center">Taxa de ocupação</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: center"><strong>1.199.195</strong><br>População de referência PNP.</td>
      <td style="text-align: center"><strong>566.971</strong><br>Egressos com vínculo formal na RAIS de referência.</td>
      <td style="text-align: center"><strong>47,28%</strong><br>Razão ocupados / total de egressos.</td>
    </tr>
  </tbody>
</table>

## Indicadores centrais

Os indicadores centrais expressam o resultado principal do módulo. Cada ficha apresenta a definição operacional, a polaridade, os níveis de agregação, o modelo matemático e as fontes de dados.

### 01 · Total de egressos · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Contabiliza os egressos da RFEPCT no período analisado. Quando o egresso apresentou mais de uma formação, considerou-se apenas a de maior nível de escolaridade para evitar dupla contagem.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor para fins de cobertura e alcance institucional. Não mede a qualidade do resultado.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Total de egressos = ∑ (egressos)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022</td></tr>
  </tbody>
</table>

### 02 · Total de ocupados · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Contabiliza os egressos com vínculo formal identificado na RAIS no ano de referência. Quando o egresso apresentou mais de um vínculo, considerou-se apenas o de maior remuneração para evitar dupla contagem.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor, desde que interpretada junto ao total de egressos e ao tamanho do grupo de referência.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Total de ocupados = ∑ (ocupados)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · RAIS 2023</td></tr>
  </tbody>
</table>

### 03 · Taxa de ocupação · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Indica a proporção de egressos com vínculo formal de trabalho em relação ao total de egressos do recorte selecionado.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor — quando o objetivo é inserção no mercado formal.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Taxa de ocupação (%) = N<sub>ocupados</sub> / N<sub>total</sub> × 100<br><em>N<sub>ocupados</sub></em>: quantidade de egressos com vínculo formal de trabalho na RAIS de referência.<br><em>N<sub>total</sub></em>: quantidade total de egressos provenientes da PNP nos anos de referência.</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · RAIS 2023</td></tr>
  </tbody>
</table>

### 04 · Raio de atuação profissional · *Descritivo*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Indica a distância entre o campus de formação e o local de trabalho do egresso.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Não se aplica. O indicador descreve mobilidade territorial e aderência regional da inserção.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Raio de atuação = r<sub>i</sub> = | D<sub>i</sub>(trabalho) − D<sub>i</sub>(campus) |<br><em>D<sub>i</sub>(trabalho)</em>: posição geoespacial associada ao local onde o egresso i exerce sua atividade profissional.<br><em>D<sub>i</sub>(campus)</em>: posição geoespacial associada ao local onde o egresso i concluiu seu curso.</td></tr>
    <tr><td><strong>Fontes</strong></td><td>IBGE — DTB 2024 · PNP 2017–2022 · RAIS 2023</td></tr>
  </tbody>
</table>

### 05 · Taxa de distorção de acesso · *Quanto menor, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Indica a proporção de egressos ocupados em postos de trabalho cujos requisitos de escolaridade são inferiores ao nível de formação concluído.</td></tr>
    <tr><td><strong>Interpretação</strong></td><td>Valores altos sugerem subutilização da formação — egressos ocupando vagas cuja exigência educacional é inferior ao seu nível concluído.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto menor, melhor.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Taxa de distorção (%) = N<sub>superqualif.</sub> / N<sub>ocupados</sub> × 100<br><em>N<sub>superqualif.</sub></em>: egressos com vínculo formal na RAIS cujos requisitos de escolaridade, segundo a CBO, são inferiores ao nível de formação concluído.<br><em>N<sub>ocupados</sub></em>: egressos com vínculo formal de trabalho na RAIS de referência.</td></tr>
    <tr><td><strong>Fontes</strong></td><td>IBGE — CBO‑2002 v. 2026 · PNP 2017–2022 · RAIS 2023</td></tr>
  </tbody>
</table>

> **Nota metodológica.** No cálculo da distorção de acesso, a especialização técnica foi tratada como ensino médio. As categorias GG1 (dirigentes com escolaridade diversa e níveis heterogêneos de competência) e GG0 (Forças Armadas, policiais e bombeiros militares) não foram comparadas, pois não possuem definição clara de competência devido à heterogeneidade dos perfis.

> **Nota interpretativa.** A taxa de distorção deve ser lida em conjunto com a taxa de ocupação e com a tipologia ocupacional. Um valor elevado pode indicar tanto inadequação entre formação e mercado quanto opção transitória do egresso por vagas de menor exigência — sobretudo em fases iniciais de carreira.

## Indicadores desagregados

Os indicadores desagregados detalham a composição interna do fenômeno identificado pelos indicadores centrais. Não medem diretamente o resultado, mas caracterizam como ele se distribui entre grupos, categorias ou contextos: natureza do vínculo, setor econômico, tipologia ocupacional, esfera administrativa, território e perfil sociodemográfico.

> **Universo de referência.** No módulo de Empregabilidade, as distribuições ocupacionais consideram apenas os egressos identificados com vínculo formal nas bases administrativas.

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th style="width: 30%; text-align: center">Indicador</th>
      <th style="width: 40%; text-align: center">Descrição</th>
      <th style="width: 30%; text-align: center">Finalidade</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Taxa de ocupação por UF</td><td>Percentual de egressos com vínculo formal em cada unidade federativa.</td><td>Identificar diferenças territoriais na inserção ocupacional formal.</td></tr>
    <tr><td>Taxa de ocupação por campus</td><td>Percentual de ocupados entre concluintes de cada campus da RFEPCT.</td><td>Comparar padrões de inserção entre unidades institucionais.</td></tr>
    <tr><td>Taxa de ocupação por curso</td><td>Percentual de ocupados entre concluintes de cada curso.</td><td>Analisar diferenças de inserção associadas às formações ofertadas.</td></tr>
    <tr><td>Taxa de ocupação por tipo de curso</td><td>Percentual de ocupados segundo a tipologia da formação cursada.</td><td>Comparar padrões de inserção entre modalidades formativas.</td></tr>
    <tr><td>Taxa de ocupação por turno</td><td>Percentual de ocupados segundo o turno de oferta do curso.</td><td>Identificar diferenças relacionadas à organização temporal da formação.</td></tr>
    <tr><td>Taxa de ocupação por sexo</td><td>Percentual de ocupados segundo sexo.</td><td>Identificar desigualdades de inserção entre grupos.</td></tr>
    <tr><td>Taxa de ocupação por faixa etária</td><td>Percentual de ocupados segundo grupos etários definidos metodologicamente.</td><td>Analisar diferenças ao longo do ciclo de vida laboral.</td></tr>
    <tr><td>Taxa de ocupação por cor ou raça</td><td>Percentual de egressos com vínculo formal segundo cor ou raça.</td><td>Identificar desigualdades de inserção ocupacional entre grupos raciais.</td></tr>
    <tr><td>Taxa de ocupação por ano de conclusão</td><td>Percentual de ocupados segundo o ano de conclusão do curso.</td><td>Acompanhar diferenças temporais de inserção ocupacional.</td></tr>
    <tr><td>Taxa de ocupação por natureza do vínculo</td><td>Distribuição dos ocupados segundo a natureza jurídica ou administrativa do vínculo.</td><td>Caracterizar o perfil institucional da inserção ocupacional.</td></tr>
    <tr><td>Taxa de ocupação por atividade econômica</td><td>Distribuição dos ocupados segundo setores econômicos do empregador (CNAE).</td><td>Identificar segmentos econômicos que concentram vínculos formais dos egressos.</td></tr>
    <tr><td>Raio de atuação por curso</td><td>Distância entre o município de formação e o município do vínculo formal, por curso.</td><td>Analisar padrões de mobilidade ocupacional associados aos cursos.</td></tr>
    <tr><td>Ocupados por UF</td><td>Distribuição absoluta ou percentual dos ocupados segundo a UF do vínculo formal.</td><td>Identificar a concentração territorial da inserção ocupacional.</td></tr>
    <tr><td>Distorção de acesso por modalidade de ensino</td><td>Diferença entre a participação dos grupos na matrícula e na população de referência.</td><td>Identificar padrões de sub-representação ou sobre-representação no acesso educacional.</td></tr>
    <tr><td>Distorção de acesso por sexo</td><td>Diferença entre a distribuição por sexo dos matriculados e a da população de referência.</td><td>Identificar desigualdades de acesso entre homens e mulheres.</td></tr>
    <tr><td>Distorção de acesso por curso e escolaridade</td><td>Diferença na composição educacional dos matriculados frente à população de referência.</td><td>Identificar assimetrias de acesso associadas ao perfil educacional dos grupos.</td></tr>
  </tbody>
</table>

**Fontes consolidadas do módulo:** IBGE — CBO‑2002 v. 2026 · IBGE — DTB 2024 · IBGE — CNAE 2.3 · PNP 2017–2022 · RAIS 2023

> **Recomendações de leitura.** 1. Sempre interprete um indicador desagregado em relação ao seu universo (egressos ocupados ou egressos totais, conforme o caso). 2. Cruzamentos sociodemográficos devem respeitar regras de segurança estatística. 3. Comparações entre UFs e campi exigem atenção à diferença de tamanho dos grupos.

[Anterior: Visão geral dos módulos](/documentacao/apresentacao/visao_geral_dos_modulos)
[Próximo: Módulo de Salários »](/documentacao/modulos/salarios)
