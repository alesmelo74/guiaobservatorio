---
layout: default
title: "Estrutura de leitura dos indicadores"
---

<!-- Parte de Navegação

Veja qual é a o nome da próxima página e da anterior e adicione abaixo no formato:

[Anterior: Nome da páginas](/documentacao/caminho_do_arquivo)
[Próximo: Nome da páginas »](/documentacao/caminho_do_arquivo) 
-->

[Anterior: Apresentação](/documentacao/apresentacao/apresentacao)

# {{ page.title }}

## Ficha padronizada

Cada indicador apresentado neste relatório segue o mesmo modelo de ficha técnica, organizado em campos padronizados. O quadro a seguir descreve cada campo e seu propósito.

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th style="width: 30%; text-align: center">Campo da ficha</th>
      <th style="width: 70%; text-align: center">Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Indicador</td><td>Nome padronizado do indicador no relatório e no painel.</td></tr>
    <tr><td>Definição</td><td>Descrição objetiva do que o indicador mede.</td></tr>
    <tr><td>Polaridade</td><td>Indica se valores maiores ou menores são desejáveis. Quando não houver direção normativa, o indicador é classificado como descritivo.</td></tr>
    <tr><td>Agregação máxima</td><td>Maior nível de consolidação recomendado, como Rede Federal, região ou UF.</td></tr>
    <tr><td>Agregação mínima</td><td>Menor nível de abertura recomendado, como campus, curso, sexo, raça ou renda — respeitando regras de segurança estatística.</td></tr>
    <tr><td>Modelo matemático</td><td>Fórmula operacional usada para cálculo do indicador.</td></tr>
    <tr><td>Variáveis, fonte e definição</td><td>Lista os componentes do cálculo, a origem dos dados e a interpretação de cada variável.</td></tr>
  </tbody>
</table>

## Convenções de polaridade

<table border="1" cellspacing="0" cellpadding="5">
  <thead>
    <tr>
      <th style="width: 33%; text-align: center">Quanto maior, melhor</th>
      <th style="width: 33%; text-align: center">Quanto menor, melhor</th>
      <th style="width: 33%; text-align: center">Descritivo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Valores elevados indicam melhor desempenho. Aplica-se a taxas de inserção, cobertura e produção.</td>
      <td>Valores elevados sinalizam disfunção. Aplica-se a distorções, sub-utilização e desigualdades.</td>
      <td>Sem orientação valorativa. Caracteriza distribuições, perfis e padrões observados.</td>
    </tr>
  </tbody>
</table>

## Segurança estatística

Em todos os recortes de agregação mínima, observam-se regras de proteção a microdados: supressão de células com baixa contagem, arredondamento controlado e limitação de cruzamentos sociodemográficos quando há risco de identificação.

[Anterior: Apresentação](/documentacao/apresentacao/apresentacao)
[Próximo: Termos utilizados »](/documentacao/termos/termos)
