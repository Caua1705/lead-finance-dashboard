PAGINAS = {
    "visao_geral": {
        "titulo": "📈 CRM de Leads",
        "cores_metricas": {
            "col1": "#7C3AED",   # Roxo - Total
            "col2": "#10B981",   # Verde - Qualificados
            "col3": "#FACC15",   # Amarelo - IA
            "col4": "#3B82F6",   # Azul - Consultor
        },
        "labels_kpis": {
            "total": "👤 Total de Leads",
            "qualificados": "✅ Leads Qualificados",
            "atendimento_ia": "🤖 Atendimento IA",
            "atendimento_consultor": "👨‍💼 Atendimento Consultor",
        },
        "insights": {
            "horario": {
                "icone": "⏰",
                "bg": "#FEF3C7",   # Amarelo claro (contraste melhor)
                "border": "#F59E0B",
            },
            "perfil": {
                "icone": "👤",
                "bg": "#ECFDF5",   # Verde claro
                "border": "#10B981",
            }
        },
        "graficos": {
            "evolucao": {
                "titulo": "### Evolução de Leads",
                "titulo_grafico": "Quantidade de Leads por Dia",
                "cor_linha": "#10B981",
                "titulo_x": "Data",
                "titulo_y": "Quantidade de Leads",
            },
            "distribuicao": {
                "titulo": "### Perfis de Leads",
                "titulo_grafico": "Distribuição de Leads por Perfil Profissional",
                "cores": {
                    "TPD": "#10B981",
                    "Estudante": "#FACC15",
                    "Dentista": "#3B82F6",
                }
            }
        }
    },
    "financeiro": {
        "titulo": "💰 Financeiro",
        "cores_metricas": {
            "col1": "#16A34A",   # Verde - Faturamento
            "col2": "#3B82F6",   # Azul - Ticket Médio
            "col3": "#6B7280",   # Cinza - Neutro
            "col4": "#F97316",   # Laranja forte
        },
        "labels_kpis": {
            "faturamento_total": "💰 Faturamento Total",
            "ticket_medio": "📊 Ticket Médio",
            "numero_vendas": "🛒 Total de Vendas",
            "porcentagem_a_vista": "💳 % à Vista",
        },
        "graficos": {
            "evolucao": {
                "titulo": "### Evolução de Vendas",
                "titulo_grafico": "Quantidade de Vendas por Dia",
                "cor_linha": "#10B981",
                "titulo_x": "Data",
                "titulo_y": "Quantidade de Vendas",
            },
            "pagamentos": {
                "titulo": "### Formas de Pagamento",
                "titulo_grafico": "Distribuição de Vendas por Forma de Pagamento",
                "cores": {
                    "Pix": "#10B981",
                    "Cartão": "#3B82F6",
                    "Boleto": "#F59E0B",
                    "Dinheiro": "#E11D48"
                }
            },
            "consultores": {
                "titulo": "### Consultores",
                "titulo_grafico": "Total de Vendas por Consultor",
                "titulo_x": "Consultores",
                "titulo_y": "Quantidade de Vendas",
                "cor": "#3B82F6"
            },
            "cursos": {
                "titulo": "### Cursos",
                "titulo_grafico": "Total de Vendas por Curso",
                "titulo_x": "Cursos",
                "titulo_y": "Quantidade de Vendas",
                "cor": "#7C3AED"
            }
        }
    }
}

URL_SUPABASE = "postgresql://postgres.unthbazstzviopslxxsz:Ca170505@aws-1-sa-east-1.pooler.supabase.com:6543/postgres"
