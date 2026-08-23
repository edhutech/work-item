# Camino de investigación para Work Items

## 1. Punto de partida

### Definición mínima provisional

**Work Item:** una unidad de trabajo de software optimizada para coding agents.

Esta definición funciona únicamente como punto de partida. La investigación no asumirá de antemano qué características hacen que una unidad de trabajo esté “optimizada”.

### Pregunta principal de investigación

> **¿Qué características debe tener una unidad de trabajo de software para estar optimizada para coding agents?**

La investigación debe permitir descubrir esas características, sus límites y las condiciones en las que son útiles.

---

## 2. Preguntas secundarias

1. ¿Qué información necesita un coding agent para ejecutar correctamente una unidad de trabajo?
2. ¿Qué efectos producen la ambigüedad, la información insuficiente y el exceso de información?
3. ¿Qué papel cumplen el objetivo, el alcance, los criterios de aceptación, las restricciones y las tareas?
4. ¿Cuánto detalle es útil antes de empezar a generar overhead o reducir flexibilidad?
5. ¿Qué debería definir la unidad de trabajo y qué debería quedar bajo decisión del coding agent?
6. ¿Cómo cambian estas necesidades según complejidad, tamaño, riesgo o alcance del trabajo?
7. ¿Qué diferencias existen entre las unidades de trabajo diseñadas para humanos y las diseñadas para coding agents?
8. ¿En qué contextos un Work Item deja de ser suficiente y necesita complementarse con una Spec u otros artifacts?

---

## 3. Construcción del marco teórico

La investigación no debe limitarse a Spec-Driven Development. Debe integrar diferentes cuerpos de conocimiento relacionados con la definición y ejecución del trabajo de software.

Áreas iniciales:

- Requirements Engineering
- Agile Requirements Engineering
- User Stories
- Acceptance Criteria
- Task and Work Decomposition
- Software Engineering Productivity
- Cognitive Load
- Information Overload
- Human-AI Collaboration
- Coding Agents
- Agent Planning
- Agent Context Management
- Software Verification
- Developer Experience

El objetivo es comprender qué sabemos actualmente sobre cómo describir, delimitar, ejecutar y evaluar trabajo de software.

---

## 4. Revisión de estándares y fuentes oficiales

Se priorizarán fuentes que representen conocimiento consolidado de ingeniería de software.

Entre ellas:

- ISO/IEC/IEEE 29148 — Requirements Engineering
- SWEBOK
- ISO/IEC 25010
- IEEE
- ACM
- documentación técnica y estándares relevantes

Estas fuentes no se utilizarán para demostrar que el Work Item es correcto, sino para identificar problemas, propiedades y criterios ya reconocidos en la ingeniería de software.

---

## 5. Revisión sistemática de literatura

Antes de comenzar la revisión se debe definir un protocolo reproducible.

### Fuentes de búsqueda sistemática

- IEEE Xplore
- ACM Digital Library
- Scopus
- Web of Science
- ScienceDirect
- SpringerLink

Google Scholar se utilizará principalmente para discovery, búsqueda de citas y snowballing.

La revisión utilizará una estrategia escalonada. Scopus será la fuente sistemática central para las 22 ramas Primary. IEEE Xplore, ACM Digital Library, Web of Science, ScienceDirect y SpringerLink deberán superar primero una validación de factibilidad de API o captura sistemática antes de participar en la calibración representativa de siete ramas. Sus roles posteriores podrán variar según la rama o el dominio de evidencia; no se asumirá que una fuente deba ejecutarse en todas las ramas. Las seis ramas Supplementary permanecerán condicionales.

### El protocolo debe definir

- preguntas de investigación;
- términos y strings de búsqueda;
- periodo de búsqueda;
- criterios de inclusión;
- criterios de exclusión;
- criterios de calidad;
- procedimiento de extracción de datos;
- tratamiento de evidencia contradictoria;
- método de síntesis.

La revisión debe buscar tanto evidencia que apoye posibles características del Work Item como evidencia que las contradiga.

---

## 6. Investigación específica sobre coding agents

Se realizará una línea específica de revisión sobre agentes de programación.

Temas prioritarios:

- ambigüedad en instrucciones;
- calidad de task descriptions;
- clarification seeking;
- planificación del agente;
- task decomposition;
- repository understanding;
- context management;
- context pollution;
- long-context behavior;
- autonomía del agente;
- over-specification;
- acceptance criteria;
- validation;
- verification;
- desempeño según tamaño y complejidad de la tarea.

El objetivo es evitar trasladar directamente modelos creados para desarrolladores humanos a coding agents sin evidencia de que funcionen de la misma manera.

---

## 7. Evidencia de desarrolladores

La experiencia de desarrolladores se utilizará como una fuente cualitativa complementaria.

### Fuentes potenciales

- GitHub Issues
- GitHub Discussions
- Reddit
- Hacker News
- foros y comunidades de Codex
- Claude Code
- Cursor
- OpenCode
- Aider
- OpenSpec
- Spec Kit
- otras herramientas relevantes

Esta evidencia no tendrá el mismo peso que un estudio científico.

Su función será identificar patrones reales de uso, fricciones, necesidades y casos extremos.

### Ejemplos de categorías que podrían emerger

- ambiguity;
- missing context;
- excessive context;
- over-planning;
- plan staleness;
- unnecessary clarification;
- context duplication;
- loss of original intent;
- difficulty resuming work;
- excessive ceremony;
- insufficient acceptance criteria;
- restricted agent autonomy.

Las categorías definitivas deben emerger de los datos y no imponerse previamente.

---

## 8. Comparación con modelos existentes de unidad de trabajo

Se estudiarán diferentes formas existentes de representar trabajo de software.

Entre ellas:

- Requirements
- Specifications
- User Stories
- Tasks
- Issues
- Tickets
- Epics
- Change Requests
- Jobs to be Done
- SDD Changes
- otros modelos relevantes

Para cada modelo se analizará:

- qué información contiene;
- qué problema intenta resolver;
- qué considera una unidad;
- cómo define finalización;
- cuánto contexto necesita;
- cuánto overhead genera;
- qué duración tiene;
- qué relación mantiene con el producto;
- qué limitaciones presenta cuando el ejecutor es un coding agent.

El objetivo no es demostrar que Work Item es superior, sino entender qué necesidad específica debería cubrir.

---

## 9. Síntesis de evidencia

Se construirá una **Evidence Matrix** para cada posible característica del Work Item.

Ejemplo:

| Posible característica | Evidencia a favor | Evidencia en contra | Calidad de evidencia | Contexto |
|---|---|---|---|---|
| Claridad | Por investigar | Por investigar | — | — |
| Alcance definido | Por investigar | Por investigar | — | — |
| Criterios verificables | Por investigar | Por investigar | — | — |
| Baja prescripción | Por investigar | Por investigar | — | — |
| Suficiencia de información | Por investigar | Por investigar | — | — |
| Bajo overhead | Por investigar | Por investigar | — | — |

Una característica no se convertirá en principio de Work Item únicamente porque resulte intuitiva.

---

## 10. Construcción del modelo teórico de Work Item

Después de analizar la evidencia se propondrá una primera definición formal.

La investigación deberá determinar:

- características esenciales;
- características opcionales;
- relaciones entre características;
- trade-offs;
- límites de aplicación;
- condiciones contextuales;
- qué información pertenece al Work Item;
- qué información debería permanecer fuera;
- cuándo el Work Item necesita complementarse con otra herramienta o artifact.

Este resultado constituirá el **modelo teórico Work Item v1**.

---

## 11. Operacionalización

Cada característica identificada deberá convertirse en algo observable o medible.

Ejemplos hipotéticos:

### Sufficiency

Posibles indicadores:

- cantidad de aclaraciones materiales;
- información faltante detectada durante la ejecución;
- rework causado por requisitos ausentes;
- bloqueos por falta de información.

### Work overhead

Posibles indicadores:

- tiempo hasta comenzar implementación;
- cantidad de artifacts necesarios;
- tamaño de la unidad de trabajo;
- contexto suministrado;
- consumo de tokens.

### Verifiability

Posibles indicadores:

- existencia de criterios verificables;
- discrepancias entre finalización declarada y validación externa;
- findings posteriores al supuesto término del trabajo.

Estos indicadores son provisionales y dependerán de las características que emerjan de la investigación.

---

## 12. Formulación de hipótesis

Las hipótesis se formularán únicamente después de construir el marco teórico y operacionalizar las variables.

Deben ser falsables.

Ejemplos ilustrativos:

> Los Work Items con criterios explícitos de finalización reducen las discrepancias entre la finalización declarada por el agente y la finalización validada externamente.

> Para cambios de baja o mediana complejidad, aumentar la cantidad de información más allá de un determinado punto no mejora proporcionalmente la calidad del resultado y sí incrementa el overhead.

> A medida que aumenta la complejidad y el impacto transversal del cambio, una unidad de trabajo ligera necesita progresivamente mayor soporte de especificación.

Estos ejemplos no deben considerarse hipótesis definitivas.

---

## 13. Diseño del alfa público como estudio empírico

El alfa público será utilizado posteriormente para contrastar las hipótesis.

El diseño de medición debe definirse antes del lanzamiento.

### Posibles datos

- tamaño del Work Item;
- complejidad del trabajo;
- agente utilizado;
- modelo utilizado;
- aclaraciones;
- tiempo hasta implementación;
- tareas generadas;
- contexto suministrado;
- tokens;
- findings;
- rework;
- reaperturas;
- successful completion.

También deberán definirse previamente:

- política de privacidad;
- telemetría;
- muestra;
- variables de control;
- instrumentos;
- encuestas;
- entrevistas.

---

## 14. Validación cuantitativa

El análisis cuantitativo buscará relaciones entre las características del Work Item y los resultados obtenidos.

Ejemplo conceptual:

```text
Work Item characteristics
          ↓
Completion quality
Clarifications
Rework
Review findings
Time
Context
Tokens
```

La eficiencia no deberá evaluarse únicamente mediante tokens.

La calidad de finalización debe permanecer como una dimensión central.

---

## 15. Validación cualitativa

La evidencia cuantitativa se complementará con análisis cualitativo.

Se estudiarán especialmente:

- Work Items que funcionaron muy bien;
- Work Items que fallaron;
- casos que requirieron muchas aclaraciones;
- trabajos con mucho rework;
- trabajos donde el usuario hubiese preferido una Spec;
- casos donde el agente necesitó mayor libertad;
- situaciones donde faltó información importante.

El objetivo es explicar por qué ocurrieron los resultados observados.

---

## 16. Triangulación

Los resultados deberán contrastarse utilizando diferentes tipos de evidencia:

```text
Scientific literature
        +
Standards
        +
Practitioner evidence
        +
Public-alpha quantitative evidence
        +
Public-alpha qualitative evidence
        ↓
Triangulated evidence
```

Una característica tendrá mayor respaldo cuando aparezca de forma consistente en fuentes independientes.

---

## 17. Refinamiento de la definición

La investigación finalizará esta primera etapa reemplazando la definición provisional:

> **A Work Item is a unit of software work optimized for coding agents.**

por una definición más precisa que establezca:

- qué significa estar optimizado;
- qué características debe poseer;
- cuáles son necesarias y cuáles contextuales;
- qué trade-offs existen;
- qué límites tiene;
- cuándo debe complementarse con otros artifacts o metodologías.

---

# Resumen del programa de investigación

1. Definición mínima provisional.
2. Pregunta principal.
3. Preguntas secundarias.
4. Marco teórico.
5. Estándares y fuentes oficiales.
6. Revisión sistemática de literatura.
7. Investigación específica sobre coding agents.
8. Evidencia cualitativa de desarrolladores.
9. Comparación con modelos existentes.
10. Síntesis mediante Evidence Matrix.
11. Modelo teórico Work Item v1.
12. Operacionalización.
13. Hipótesis falsables.
14. Diseño del estudio del alfa público.
15. Validación cuantitativa.
16. Validación cualitativa.
17. Triangulación.
18. Refinamiento de la definición.

---

## Principio metodológico

> **La investigación no debe diseñarse para demostrar que Work Items funcionan, sino para descubrir qué características necesita una unidad de trabajo optimizada para coding agents, bajo qué condiciones esas características producen mejores resultados y dónde dejan de ser suficientes.**
