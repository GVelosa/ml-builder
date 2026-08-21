
from src.models.ml_projects import MLProject

# Ordem oficial das etapas do projeto.
# A posição de cada item define quais etapas precisam vir antes dele.
STEPS = [
    "upload",
    "config",
    "preprocessing",
    "model_parameters",
    "training",
    "results",
]

ROUTE_STEPS = {
    "/upload": "upload",
    "/config": "config",
    "/preprocessing": "preprocessing",
    "/model_parameters": "model_parameters",
    "/training": "training",
    "/results": "results",
}


def validate_step(step: str) -> None:
    """Interrompe a execução quando o nome de uma etapa não existe."""

    if step not in STEPS:
        raise ValueError(f"Etapa desconhecida: {step}")


def is_step_completed(ml_project: MLProject, step: str) -> bool:
    """Informa se uma etapa já foi marcada como concluída."""

    validate_step(step)
    return step in ml_project.completed_steps


def complete_step(ml_project: MLProject, step: str) -> None:
    """Marca uma etapa válida como concluída."""

    validate_step(step)
    ml_project.completed_steps.add(step)


def get_required_steps(step: str) -> list[str]:
    """Retorna todas as etapas que precisam estar concluídas antes da etapa recebida."""

    validate_step(step)
    step_index = STEPS.index(step)
    return STEPS[:step_index]


def can_access_step(ml_project: MLProject, step: str) -> bool:
    """Permite acesso somente quando todas as etapas anteriores foram concluídas."""

    required_steps = get_required_steps(step)
    return all(
        required_step in ml_project.completed_steps
        for required_step in required_steps
    )


def can_access_route(ml_project: MLProject, route: str) -> bool:
    """Verifica uma rota; rotas que não pertencem ao fluxo permanecem livres."""

    step = ROUTE_STEPS.get(route)

    if step is None:
        return True

    return can_access_step(ml_project, step)


def get_step_status(ml_project: MLProject, step: str) -> str:
    """Retorna completed, available ou locked para uso na interface."""

    if is_step_completed(ml_project, step):
        return "completed"

    if can_access_step(ml_project, step):
        return "available"

    return "locked"
