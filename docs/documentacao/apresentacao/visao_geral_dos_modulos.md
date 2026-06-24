---
layout: default
title: "Visão geral dos módulos"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

-->

# {{ page.title }}

A plataforma é organizada em cinco módulos analíticos. Cada módulo responde a uma dimensão específica da trajetória dos egressos e combina indicadores centrais com indicadores desagregados que detalham o resultado por grupos, atributos ou contextos.

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th style="width: 18%; text-align: center">Módulo</th>
      <th style="width: 47%; text-align: center">Descrição</th>
      <th style="width: 35%; text-align: center">Indicadores centrais</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="{{ "/documentacao/modulos/empregabilidade" | relative_url }}"><strong>Empregabilidade</strong></a></td>
      <td>Mensura a inserção dos egressos no mercado de trabalho formal a partir de vínculos empregatícios registrados em bases administrativas.</td>
      <td>Total de egressos · Total de ocupados · Taxa de ocupação · Raio de atuação · Distorção de acesso</td>
    </tr>
    <tr>
      <td><a href="{{ "/documentacao/modulos/salarios" | relative_url }}"><strong>Salários</strong></a></td>
      <td>Mensura a remuneração dos egressos ocupados a partir das informações salariais registradas em vínculos formais identificados na RAIS.</td>
      <td>Massa salarial · Salário médio · Mediana · Média logarítmica · Desvio padrão · Salário relativo</td>
    </tr>
    <tr>
      <td><a href="{{ "/documentacao/modulos/empreendedorismo" | relative_url }}"><strong>Empreendedorismo</strong></a></td>
      <td>Mensura a vinculação formal de egressos a quadros societários de empresas e identifica a atividade empresarial registrada em bases administrativas.</td>
      <td>Total de empreendedores · Taxa de empreendedorismo · Empresas criadas · Capital social médio</td>
    </tr>
    <tr>
      <td><a href="{{ "/documentacao/modulos/trajetoria_academica" | relative_url }}"><strong>Trajetória Acadêmica</strong></a></td>
      <td>Mensura a continuidade da formação educacional dos egressos por meio da identificação de vínculos acadêmicos posteriores à diplomação.</td>
      <td>Total com trajetória · Taxa de trajetória · Fluxos acadêmicos · Movimentação e permanência</td>
    </tr>
    <tr>
      <td><a href="{{ "/documentacao/modulos/producao_academica" | relative_url }}"><strong>Produção Acadêmica</strong></a></td>
      <td>Mensura a atividade técnico-científica dos egressos por meio da identificação de produções registradas em bases curriculares e científicas.</td>
      <td>Egressos com Lattes · Total de produção · Egressos com produção · Média de produção</td>
    </tr>
  </tbody>
</table>

## Integração de bases

PNP · RAIS · CBO · IBGE · CNAE · CNPJ (Receita Federal) · Plataforma Carolina Bori · Plataforma Lattes · INEP · CAPES.

O modelo analítico integra bases administrativas, educacionais, ocupacionais e científicas para construir indicadores multidimensionais — com pareamento por CPF e harmonização temporal.

