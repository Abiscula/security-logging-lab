from fastapi import Request

async def request_context_middleware(request: Request, call_next):
  # Captura IP do cliente
  request.state.ip = request.client.host if request.client else None

  # Captura User-Agent
  request.state.user_agent = request.headers.get("user-agent")

  # Continua o fluxo da requisição
  response = await call_next(request)
  return response