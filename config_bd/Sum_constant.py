# from sqlalchemy import select, update, delete
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from config_bd.BaseModel import SumConstant
#
#
# async def orm_select_sum_constant(session: AsyncSession):
#     query = select(SumConstant).where(SumConstant.id == 1)
#     result = await session.execute(query)
#     return result.scalars().one()
