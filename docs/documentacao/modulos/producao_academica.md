---
layout: default
title: "Módulo de Produção Acadêmica"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas](/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »](/documentacao/caminho_do_arquivo) 
-->

[Anterior: Módulo de Trajetória Acadêmica](/documentacao/modulos/trajetoria_academica)

# {{ page.title }}

> **Produção bibliográfica, técnica e propriedade intelectual.** Mensura a atividade técnico-científica dos egressos da RFEPCT por meio da identificação de produções registradas em bases curriculares e científicas — especialmente no Currículo Lattes.

## Escopo e leitura

O módulo mensura a atividade técnico-científica dos egressos da RFEPCT por meio da identificação de produções registradas em bases curriculares e científicas. Utiliza os egressos como população de referência e os registros de produção acadêmica como evidência operacional de atividade científica.

O módulo contempla indicadores relacionados à produção bibliográfica, produção técnica, participação em eventos científicos, orientação acadêmica, inovação e demais atividades registradas nos currículos dos egressos. As análises podem ser realizadas em diferentes horizontes temporais e níveis de agregação institucional, territorial e sociodemográfica.

A metodologia baseia-se no pareamento entre registros da Plataforma Nilo Peçanha e currículos identificados na Plataforma Lattes. Os indicadores dependem da disponibilidade, atualização e consistência das informações declaradas nas bases utilizadas.

Os indicadores não capturam produções científicas não registradas ou não declaradas nos currículos analisados. Os resultados devem ser interpretados como medidas de produção técnico-científica formalmente registrada — condicionados à atualização e à completude das informações declaradas pelos próprios titulares dos currículos.

### Estrutura do módulo

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 30%"><strong>Indicadores centrais</strong></td><td>Total de egressos com Currículo Lattes · Total de egressos · Taxa de egressos com Lattes · Total de Produção Acadêmica · Total de egressos com Produção · Média de Produção Acadêmica.</td></tr>
    <tr><td><strong>Indicadores desagregados</strong></td><td>Lattes por UF · curso · tipo de curso · turno · campus · categoria · tipo de produção bibliográfica · tipo de produção técnica · tipo de propriedade intelectual.</td></tr>
  </tbody>
</table>

> **Limites de cobertura.** A produção captada depende da existência e atualização do Currículo Lattes do egresso. A não identificação no Lattes não significa ausência de produção, apenas ausência de registro nas bases utilizadas.

## Indicadores centrais

### 01 · Total de egressos com Currículo Lattes · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Contabiliza o número de egressos da RFEPCT com Currículo Lattes identificado.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor para fins de rastreabilidade acadêmica dos egressos. Não mede produtividade científica.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Total de egressos com Lattes = ∑ (egressos_Lattes)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · Plataforma Lattes</td></tr>
  </tbody>
</table>

### 02 · Total de egressos · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Contabiliza os egressos da RFEPCT no período analisado. Quando o egresso apresentou mais de uma formação, considerou-se apenas a de maior nível de escolaridade para evitar dupla contagem.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor para fins de cobertura analítica e tamanho da base. Não mede desempenho acadêmico ou científico.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Total de egressos = ∑ (egressos)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · Plataforma Lattes</td></tr>
  </tbody>
</table>

### 03 · Taxa de egressos com Currículo Lattes · *Descritivo*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Mede o percentual de egressos da RFEPCT com Currículo Lattes identificado em relação ao total de egressos da base PNP.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Neutra. Indicador de referência utilizado para composição analítica dos demais indicadores do módulo.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>TX_Lattes = ∑ (egressos_Lattes) / ∑ (egressos)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · Plataforma Lattes</td></tr>
  </tbody>
</table>

### 04 · Total de Produção Acadêmica · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Soma a produção absoluta dos egressos no Currículo Lattes, categorizada em: bibliográfica, técnica e propriedade intelectual.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor. Valores mais elevados indicam maior volume de produção acumulada pelos egressos.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Total de Produção Acadêmica = ∑ (prod_bibliográfica) + ∑ (prod_técnica) + ∑ (prop_intelectual)<br><em>prod_bibliográfica</em>: publicações acadêmicas e técnico-científicas vinculadas aos egressos.<br><em>prod_técnica</em>: produtos, processos, serviços e materiais técnico-profissionais desenvolvidos pelos egressos.<br><em>prop_intelectual</em>: ativos intelectuais registrados ou depositados pelos egressos em órgãos de proteção da propriedade industrial e intelectual.</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · Plataforma Lattes</td></tr>
  </tbody>
</table>

### 05 · Total de egressos com Produção Acadêmica · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Contabiliza os egressos da RFEPCT com pelo menos uma produção registrada na Plataforma Lattes — seja ela bibliográfica, técnica ou de propriedade intelectual.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor. Valores elevados indicam que um número maior de egressos da RFEPCT está engajado em atividades de produção acadêmica, científica, tecnológica ou cultural — o que reflete positivamente sobre o impacto formativo das instituições.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Egressos com Produção = ∑ egressos da RFEPCT com ao menos uma produção cadastrada no Lattes</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · Plataforma Lattes</td></tr>
  </tbody>
</table>

### 06 · Média de Produção Acadêmica · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Calcula a média de produções registradas na Plataforma Lattes entre os egressos da RFEPCT que possuem ao menos uma produção cadastrada.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor. Valores elevados indicam maior intensidade produtiva entre os egressos com ao menos uma produção cadastrada no Lattes.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Média de Produção = Total de produções registradas no Lattes / Total de egressos com ao menos uma produção</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · Plataforma Lattes</td></tr>
  </tbody>
</table>

## Indicadores desagregados

Detalham a composição interna dos resultados identificados pelos indicadores centrais. Caracterizam como a produção se distribui segundo sexo, faixa etária, curso, área do conhecimento, nível de formação, território, tipo de produção ou características institucionais.

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th style="width: 30%; text-align: center">Indicador</th>
      <th style="width: 40%; text-align: center">Descrição</th>
      <th style="width: 30%; text-align: center">Finalidade</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Taxa de egressos com Lattes por UF</td><td>Percentual de egressos com Currículo Lattes identificado segundo a UF.</td><td>Identificar diferenças territoriais na presença de registros curriculares.</td></tr>
    <tr><td>Taxa de egressos com Lattes por curso</td><td>Percentual de egressos com Currículo Lattes segundo o curso concluído.</td><td>Comparar a presença de registros curriculares entre diferentes formações.</td></tr>
    <tr><td>Taxa de egressos com Lattes por tipo de curso</td><td>Percentual de egressos com Lattes segundo a tipologia da formação cursada.</td><td>Analisar diferenças de vinculação à Plataforma Lattes entre modalidades formativas.</td></tr>
    <tr><td>Média de produção acadêmica por UF</td><td>Média de produções registradas nos currículos Lattes dos egressos segundo a UF.</td><td>Identificar diferenças territoriais na intensidade da produção registrada.</td></tr>
    <tr><td>Média de produção acadêmica por campus</td><td>Média de produções nos currículos Lattes segundo o campus de origem.</td><td>Comparar a intensidade da produção entre unidades institucionais.</td></tr>
    <tr><td>Número de produção por curso</td><td>Quantidade de produções nos currículos Lattes segundo o curso concluído.</td><td>Identificar cursos com maior concentração de produção acadêmica registrada.</td></tr>
    <tr><td>Número de produção por tipo de curso</td><td>Quantidade de produções nos currículos Lattes segundo a tipologia da formação.</td><td>Comparar o volume de produção entre modalidades formativas.</td></tr>
    <tr><td>Número de produção por turno</td><td>Quantidade de produções nos currículos Lattes segundo o turno de oferta do curso.</td><td>Identificar diferenças no volume de produção associadas ao turno de formação.</td></tr>
    <tr><td>Número de produção por categoria</td><td>Quantidade de produções segundo categorias gerais — bibliográfica, técnica ou propriedade intelectual.</td><td>Caracterizar a composição geral da produção acadêmica dos egressos.</td></tr>
    <tr><td>Número de produção por tipo de produção bibliográfica</td><td>Quantidade de produções bibliográficas segundo o tipo — artigos, livros, capítulos ou trabalhos em eventos.</td><td>Identificar os principais formatos de produção bibliográfica.</td></tr>
    <tr><td>Número de produção por tipo de produção técnica</td><td>Quantidade de produções técnicas segundo o tipo — relatórios, softwares, produtos tecnológicos ou trabalhos técnicos.</td><td>Identificar os principais formatos de produção técnica.</td></tr>
    <tr><td>Número de produção por tipo de propriedade intelectual</td><td>Quantidade de registros segundo o tipo — patentes, programas de computador, marcas ou desenhos industriais.</td><td>Caracterizar a participação dos egressos em atividades de inovação formalmente registradas.</td></tr>
  </tbody>
</table>

**Fontes consolidadas do módulo:** PNP 2017–2022 · Plataforma Lattes · CNPq — Tabela de Áreas do Conhecimento · CAPES — GT Produção Técnica

> **Recomendações de leitura.** 1. Apresentar a taxa de cobertura Lattes junto às medidas de produção — para evitar leituras distorcidas em recortes com baixa rastreabilidade. 2. Distinguir produção bibliográfica, técnica e propriedade intelectual nas análises agregadas. 3. Considerar o tempo decorrido desde a conclusão como variável de controle em análises de produtividade.

[Anterior: Módulo de Trajetória Acadêmica](/documentacao/modulos/trajetoria_academica)
[Próximo: Considerações finais »](/documentacao/consideracoes_finais/consideracoes_finais)
