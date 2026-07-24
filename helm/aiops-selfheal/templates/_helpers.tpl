{{/*
Expand the chart name.
*/}}
{{- define "aiops-selfheal.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Create a fullname.
*/}}
{{- define "aiops-selfheal.fullname" -}}
{{- if .Values.fullnameOverride }}
{{- .Values.fullnameOverride | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s" (include "aiops-selfheal.name" .) }}
{{- end }}
{{- end }}

{{/*
Common labels.
*/}}
{{- define "aiops-selfheal.labels" -}}
app.kubernetes.io/name: {{ include "aiops-selfheal.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/version: {{ .Chart.AppVersion }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ .Chart.Name }}-{{ .Chart.Version }}
{{- end }}