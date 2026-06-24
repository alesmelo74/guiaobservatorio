---
layout: default
title: "Módulo de Trajetória Acadêmica"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas](/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »](/documentacao/caminho_do_arquivo) 
-->

[Anterior: Módulo de Empreendedorismo](/documentacao/modulos/empreendedorismo)

# {{ page.title }}

> **Continuidade da formação educacional.** Mensura a continuidade da formação educacional dos egressos da RFEPCT por meio da identificação de vínculos acadêmicos em cursos de graduação e pós-graduação registrados em bases administrativas e curriculares.

## Escopo e leitura

O módulo mensura a continuidade da formação educacional dos egressos da RFEPCT por meio da identificação de vínculos acadêmicos em cursos de graduação e pós-graduação registrados em bases administrativas e curriculares.

O módulo contempla indicadores relacionados ao prosseguimento dos estudos, níveis de formação alcançados, mobilidade acadêmica e continuidade da trajetória educacional dos egressos. As análises podem ser realizadas em diferentes horizontes temporais e níveis de agregação institucional, territorial e sociodemográfica.

A metodologia baseia-se no pareamento entre registros da Plataforma Nilo Peçanha, bases educacionais (CAPES, Plataforma Carolina Bori) e currículos identificados na Plataforma Lattes. Os indicadores dependem da disponibilidade, atualização e consistência das informações registradas nas bases utilizadas.

Os indicadores não capturam trajetórias acadêmicas não registradas administrativamente ou não declaradas nas bases de origem. Os resultados devem ser interpretados como medidas de continuidade formal da formação acadêmica, restritas aos registros identificáveis nas bases utilizadas.

### Estrutura do módulo

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 30%"><strong>Indicadores centrais</strong></td><td>Total de egressos com trajetória · Total de egressos na PNP · Taxa de trajetória acadêmica · Fluxos acadêmicos · Taxa de movimentação e permanência.</td></tr>
    <tr><td><strong>Indicadores desagregados</strong></td><td>Trajetórias por curso · tipo de curso · turno · status acadêmico · tipo de trajetória (vertical/horizontal/reversão) · nível subsequente.</td></tr>
  </tbody>
</table>

> **Tipos de trajetória.** *Progressão vertical*: curso de destino de nível superior ao do curso concluído na RFEPCT. *Progressão horizontal*: curso de destino de mesmo nível. *Reversão de nível*: curso de destino de nível anterior.

## Indicadores centrais

### 01 · Total de egressos com trajetória acadêmica identificada · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Contabiliza o total de egressos que tiveram continuidade acadêmica stricto sensu identificada nas bases de pós-graduação ou reconhecimento de trajetória.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor. Mede a extensão e o alcance da continuidade acadêmica — indicador estritamente quantitativo, não avalia qualidade.</td></tr>
    <tr><td><strong>Observação de uso</strong></td><td>Deve ser interpretado junto ao total de egressos, pois instituições maiores tendem a apresentar maior volume absoluto.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Total com trajetória = ∑ (quantidade_traj)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>CAPES · PNP 2017–2022 · Plataforma Carolina Bori</td></tr>
  </tbody>
</table>

### 02 · Total de egressos · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Contabiliza o total de egressos registrados na base PNP no contexto de análise, sem exclusão de dupla formação, pois o indicador considera a trajetória acadêmica do egresso ao longo do tempo. Serve como denominador da taxa de trajetória acadêmica.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor apenas para fins de cobertura da base. Não mede desempenho acadêmico.</td></tr>
    <tr><td><strong>Observação de uso</strong></td><td>Deve ser usado como base de comparação para evitar interpretações distorcidas de totais absolutos.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Total de egressos = ∑ (quantidade_egressos)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>PNP 2017–2022 · Plataforma Carolina Bori</td></tr>
  </tbody>
</table>

### 03 · Taxa de trajetória · *Quanto maior, melhor*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Mede a proporção de egressos da base PNP com trajetória acadêmica identificada em bases de continuidade de estudos. O numerador considera egressos identificados via CAPES e Carolina Bori; o denominador, o total de egressos na base PNP no contexto de filtro selecionado.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Quanto maior, melhor. Indica maior continuidade acadêmica identificada entre os egressos.</td></tr>
    <tr><td><strong>Observação de uso</strong></td><td>É o indicador central do módulo. Deve ser analisado com filtros de ano de conclusão, instituição, UF, região, nível de ensino, cor ou raça, sexo, faixa etária, renda familiar, turno e modalidade.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Taxa de trajetória = ∑ (quantidade_traj) / ∑ (quantidade_egressos)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>CAPES · PNP 2017–2022 · Plataforma Carolina Bori</td></tr>
  </tbody>
</table>

### 04 · Fluxos acadêmicos · *Descritivo*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Combinação entre o nível/modalidade de formação concluído pelo egresso na RFEPCT (curso de origem) e o nível/modalidade de formação em que ele foi identificado posteriormente (curso de destino), compondo o percurso educacional observado.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Não aplicável. O indicador possui caráter descritivo e analítico — destinado à identificação dos padrões de continuidade e mobilidade acadêmica dos egressos.</td></tr>
    <tr><td><strong>Observação de uso</strong></td><td>O denominador exclui abandono e outras situações não classificadas como Titulado ou Matriculado no modelo DAX.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Fluxo Acadêmico = ∑ (quantidade de egressos por combinação origem → destino)</td></tr>
    <tr><td><strong>Fontes</strong></td><td>CAPES · PNP 2017–2022 · Plataforma Carolina Bori</td></tr>
  </tbody>
</table>

### 05 · Taxa de movimentação e permanência · *Interpretativo*

<table border="1" cellspacing="0" cellpadding="5">
  <tbody>
    <tr><td style="width: 25%"><strong>Definição</strong></td><td>Indica a mobilidade geográfica dos egressos no sistema de educação superior, refletindo o deslocamento interestadual e interinstitucional.</td></tr>
    <tr><td><strong>Polaridade</strong></td><td>Interpretativa. Maiores taxas de permanência podem indicar fortalecimento das redes locais de formação e capacidade regional de retenção acadêmica. Maiores taxas de movimentação podem indicar ampliação da mobilidade acadêmica e busca por oportunidades formativas em outras unidades federativas.</td></tr>
    <tr><td><strong>Observação de uso</strong></td><td>A UF apresentada na linha principal representa a UF de origem do egresso na RFEPCT. As linhas detalhadas representam as UFs de destino identificadas nas trajetórias. Os percentuais de movimentação e permanência são complementares, totalizando 100% para cada UF analisada.</td></tr>
    <tr><td><strong>Agregação máxima / mínima</strong></td><td>Rede Federal / Unidade · campus</td></tr>
    <tr><td><strong>Modelo matemático</strong></td><td>Taxa de movimentação (%) = [ ∑ (qtd_egressos com UF_destino ≠ UF_origem) / ∑ (qtd_egressos com trajetória) ] × 100<br>Taxa de permanência (%) = [ ∑ (qtd_egressos com UF_destino = UF_origem) / ∑ (qtd_egressos com trajetória) ] × 100</td></tr>
    <tr><td><strong>Fontes</strong></td><td>CAPES · PNP 2017–2022 · Plataforma Carolina Bori</td></tr>
  </tbody>
</table>

## Indicadores desagregados

Detalham a composição interna dos resultados identificados pelos indicadores centrais. Caracterizam como as trajetórias acadêmicas se distribuem segundo sexo, faixa etária, curso de origem, nível de formação, área do conhecimento, território ou características institucionais.

> **Universo de referência.** As análises consideram exclusivamente os registros acadêmicos identificados nas bases administrativas e curriculares utilizadas, estando condicionadas à disponibilidade, atualização e consistência das informações registradas.

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th style="width: 30%; text-align: center">Indicador</th>
      <th style="width: 40%; text-align: center">Descrição</th>
      <th style="width: 30%; text-align: center">Finalidade</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Taxa de trajetórias por curso</td><td>Percentual de egressos com continuidade acadêmica identificada em relação ao total na PNP, segmentado por curso de origem.</td><td>Comparar a continuidade entre cursos e identificar formações com maior prosseguimento.</td></tr>
    <tr><td>Taxa de trajetórias por tipo de curso</td><td>Percentual de egressos com continuidade segundo o nível ou modalidade do curso de origem.</td><td>Analisar diferenças de prosseguimento entre tipos de curso e níveis educacionais.</td></tr>
    <tr><td>Taxa de trajetórias por turno</td><td>Percentual de egressos com continuidade segundo o turno de realização do curso de origem.</td><td>Identificar variações associadas ao turno de oferta da formação inicial.</td></tr>
    <tr><td>Taxa de trajetórias por status acadêmico</td><td>Percentual de egressos com trajetória segundo a situação atual do novo vínculo — matriculado, titulado ou equivalente.</td><td>Acompanhar a condição atual da trajetória e identificar a proporção de egressos que concluíram novas formações.</td></tr>
    <tr><td>Distribuição dos tipos de trajetórias</td><td>Proporção de egressos classificados segundo a direção do fluxo formativo — progressão vertical, horizontal ou reversão de nível.</td><td>Avaliar se a continuidade representa elevação de nível, permanência ou retorno a formação anterior.</td></tr>
    <tr><td>Fluxo acadêmico</td><td>Percentual de egressos com continuidade segundo o nível alcançado — graduação, mestrado, doutorado, mestrado/doutorado profissional.</td><td>Identificar os níveis educacionais mais acessados pelos egressos que deram continuidade.</td></tr>
    <tr><td>Distribuição das trajetórias por curso e grau acadêmico</td><td>Apresenta a distribuição das trajetórias acadêmicas dos egressos segundo o curso de origem e o grau acadêmico alcançado na formação subsequente.</td><td>Comparar diferenças entre cursos, identificar perfis de progressão educacional e apoiar análises sobre mobilidade acadêmica dos egressos da RFEPCT.</td></tr>
  </tbody>
</table>

**Fontes consolidadas do módulo:** PNP 2017–2022 · CAPES · Plataforma Carolina Bori · INEP

[Anterior: Módulo de Empreendedorismo](/documentacao/modulos/empreendedorismo)
[Próximo: Módulo de Produção Acadêmica »](/documentacao/modulos/producao_academica)
